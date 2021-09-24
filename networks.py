import torch
import torch.nn as nn
import torch.nn.functional as F
import math
import pdb

def convBlock(dim_in, dim_out):
    block = nn.Sequential(
        nn.Conv2d(dim_in, dim_out, 4, 2, 1),
        nn.BatchNorm2d(dim_out),
        nn.LeakyReLU(),
    )
    return block

def convTransposeBlock(dim_in, dim_out):
    block = nn.Sequential(
        nn.ConvTranspose2d(dim_in, dim_out, 4, 2, 1),
        nn.BatchNorm2d(dim_out),
        nn.ReLU(),
    )
    return block

class Generator(nn.Module):
    def __init__(self, im_size=128, feat_size_min=4, nf_min=64, nf_max=1024):
        super(Generator, self).__init__()
        assert im_size >= 128
        num_layers = int(math.log2(im_size//feat_size_min)) # 5
        num_layers_base = num_layers - int(math.log2(nf_max//nf_min)) # 5-4=1
        
        encode_layers = []
        encode_layers.append(convBlock(3, nf_min))
        for _ in range(num_layers_base-1):
            encode_layers.append(convBlock(nf_min, nf_min))
        nf = nf_min
        for _ in range(num_layers - num_layers_base):
            encode_layers.append(convBlock(nf, nf*2))
            nf = nf*2
        self.encode_layers = nn.ModuleList(encode_layers)
        
        decode_layers = []
        decode_layers.append(convTransposeBlock(nf_max+1, nf_max))
        nf = nf_max
        for _ in range(num_layers - num_layers_base - 1):
            decode_layers.append(convTransposeBlock(nf+nf//2, nf//2))
            nf = nf//2
        # nf=128
        for _ in range(num_layers_base-1):
            decode_layers.append(convTransposeBlock(nf + nf_min, nf_min))
            nf = nf_min
        decode_layers.append(nn.Sequential(
            nn.ConvTranspose2d(nf + nf_min, 3, 4, 2, 1),
            nn.Tanh(),
        ))
        self.decode_layers = nn.ModuleList(decode_layers)

        self.feat_size_min = feat_size_min

    def encode(self, img):
        # img = [B, 3, im_size, im_size]
        feats_in = []
        x = img
        for block in self.encode_layers:
            x = block(x)
            feats_in.append(x)
        return feats_in
    
    def decode(self, feats_in, a):
        bs = a.shape[0]
        a = a.view(bs, 1, 1, 1).repeat(1, 1, self.feat_size_min, self.feat_size_min)
        # a = [bs, 1, 4, 4]
        feat_new = a
        for feat_old, block in zip(feats_in[::-1], self.decode_layers):
            feat_cat = torch.cat([feat_new, feat_old], dim=1)
            feat_new = block(feat_cat)
        return feat_new

    def forward(self, x, a):
        # x = [B, 3, 256, 256]
        # a = [B]
        return self.decode(self.encode(x), a)


def conv_inst_lrelu(dim_in, dim_out):
    block = nn.Sequential(
        nn.Conv2d(dim_in, dim_out, 4, 2, 1),
        nn.InstanceNorm2d(dim_out),
        nn.LeakyReLU(),
    )
    return block

class Discriminator(nn.Module):
    def __init__(self, im_size=128, feat_size_min=4, nf_min=64, nf_max=1024):
        super(Discriminator, self).__init__()
        assert im_size >= 128
        num_layers = int(math.log2(im_size//feat_size_min)) # 5
        num_layers_base = num_layers - int(math.log2(nf_max//nf_min)) # 5-4=1

        convs = []
        convs.append(conv_inst_lrelu(3, nf_min))
        for _ in range(num_layers_base-1):
            convs.append(conv_inst_lrelu(nf_min, nf_min))
        nf = nf_min
        for _ in range(num_layers - num_layers_base):
            convs.append(conv_inst_lrelu(nf, nf*2))
            nf = nf*2
        self.convs = nn.ModuleList(convs)
        
        self.gan = nn.Sequential(
            nn.Linear(nf_max*feat_size_min*feat_size_min, nf_max),
            nn.LeakyReLU(),
            nn.Linear(nf_max, 1)
        )
        self.att = nn.Sequential(
            nn.Linear(nf_max*feat_size_min*feat_size_min, nf_max),
            nn.LeakyReLU(),
            nn.Linear(nf_max, 1),
            nn.Sigmoid()
        )

    def forward(self, x):
        # x = [B, 3, im_size, im_size]
        for block in self.convs:
            x = block(x)
        h = x.view(x.shape[0], -1)
        # h = [B, nf_max, feat_size_min, feat_size_min]
        out_gan = self.gan(h).view(-1)
        out_att = self.att(h).view(-1)
        return out_gan, out_att

if __name__ == '__main__':
    im_size = 512
    x = torch.randn(4,3,im_size,im_size)
    a = torch.ones(4).float()
    netG = Generator(im_size=im_size)
    netD = Discriminator(im_size=im_size)
    img_hat = netG(x, a)
    a, b = netD(x)
    print(img_hat.shape)
    pdb.set_trace()