import torch
from PIL import Image
import numpy as np
from networks import Generator
import cv2
from torchvision import transforms

def process_image(image_path):
    netG = Generator().eval()
    netG.load_state_dict(torch.load('cycle.ckpt'))
    model = netG

    try:
        img = cv2.imread(image_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    except:
        print('[ERROR] unable to load image from', image_path)
        return None
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    if len(faces) == 0:
        print('[ERROR] no face detected!')
        return None

    if len(faces) > 1:
        print('[ERROR] more than one face detected!')
        return None
    x, y, w, h = faces[0]
    crop_img = img[y:y+h, x:x+w]
    tgt_w = 128.0
    scale = tgt_w/w
    scaled_img = cv2.resize(crop_img, (0,0), fx=scale, fy=scale)
    image = Image.fromarray(scaled_img[:,:,::-1])

    # image.show()
    normalize = transforms.Normalize(
    mean=[0.5, 0.5, 0.5],
    std=[0.5, 0.5, 0.5])
    transform = transforms.Compose([
        transforms.Resize(128),
        transforms.CenterCrop(128),
        transforms.ToTensor(),
        normalize
    ])
    img_in = transform(image)
    with torch.no_grad():
        model_output = model(img_in.unsqueeze(0), torch.tensor([1.0]).float())
        img_np = np.floor((model_output.squeeze(0).cpu().numpy().transpose(1,2,0) + 1.0) * 0.5 * 255).astype(np.uint8)
        img_out = Image.fromarray(img_np)
    image.save('./static/input.jpg')
    img_out.save('./static/output.jpg')
    # img_out.show()
    return img_out
