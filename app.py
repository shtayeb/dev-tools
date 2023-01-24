from flask import Flask, render_template, send_file,request
from PIL import Image, ImageDraw, ImageFont
import io
from webcolors import rgb_to_hex
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('docs/index.html')



@app.route('/generate-image')
def generate_banner():
   
    width = request.args.get('width',default=1920,type=int) 
    height = request.args.get('height',default=1080,type=int) 
    title = request.args.get('text')
    border_color = request.args.get('border_color',default="purple",type=str) 
    border_width = request.args.get('border_width',default=40,type=int) 

    # Create a new image with a size of width*height pixel
    image = Image.new('RGB', (width, height), color = (255, 255, 255))

    # Add the title to the image
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(r"Epilogue-Bold.ttf", 32)
    w, h = draw.textsize(title, font)
    draw.text(((width-w)/2,(height-h)/2), title, font=font, fill=(0,0,0),antialias=True)

    # draw.text(((width-w)/2,(height-h)/3), author, font=font, fill=(0,0,0),antialias=True)
    # draw.text(((width-w)/2,(height-h)/4), date, font=font, fill=(0,0,0),antialias=True)
 
    # Add a linear gradient background
    # for i in range(height): 
    #     color = (int(i/3),0,int(166-(i/3)))
    #     color = int(rgb_to_hex(color)[1:], 16)
    #     draw.rectangle([0, i, width, i+1], fill=color)

    # add purple border to top and bottom
    color = (border_color) # purple color
    draw = ImageDraw.Draw(image)
    draw.line([(0, 0), (width, 0)], fill=color, width=border_width) # top border
    draw.line([(0, height), (width, height)], fill=color, width=border_width) # bottom border

    # Add the author name and avatar
    # font = ImageFont.truetype(r"Epilogue-Bold.ttf", 18)
    # avatar = Image.open(avatar)
    # avatar = avatar.resize((50,50))
    # # make the avatar round
    # mask = Image.new('L', avatar.size, 0)
    # draw = ImageDraw.Draw(mask) 
    # draw.ellipse((0, 0) + avatar.size, fill=255)
    # avatar.putalpha(mask)
    # image.paste(avatar, (20, 200), avatar)

  
    
    
    # Save the image
    img_io = io.BytesIO()
    image.save(img_io, 'PNG', quality=100)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/jpeg')


if __name__ == '__main__':
    app.run(debug=True)
