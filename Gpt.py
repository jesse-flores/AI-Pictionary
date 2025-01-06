import openai
import base64
import cv2
from time import sleep
key = cv2.waitKey(1)
webcam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
openai.api_key = *REMOVED*;


def encode_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

image_path = "C:/Users/USERNAME/Python_workspace/saved_img.jpg"
image_path = image_path.replace('"', '')
encode_image = encode_to_base64(image_path)    
# print(f"Size in bytes of the image is : {encode_image.__sizeof__()/1024:2.2f}")

# # Getting the base64 string
# base64_image = encode_image(image_path)
def confidence(encode_image):
  
  response = openai.ChatCompletion.create(
    model="gpt-4o-mini",
    messages=[
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "You will recieve an image of some extremely simple lego item built by kids ages 6 to 11. Return an integer value representing the percent likelihood that the image is what you think it is and return a one word string of what you think it is. The integer should have no string preceding it. Also print out the item and the integer on the same line seperated by a comma in the order: integer, a + item. If you don't know what it is return: 0, idk ",
          },
          {
            "type": "image_url",
            "image_url": {
              "url":  f"data:image/jpeg;base64,{encode_image}"
            },
          },
        ],
      }
    ],
  )
  response = response.choices[0].message.content
 
  return response




def percentage(response):
   percentage = 0
   item = ''
   for i in range(len(response)):
      if response[i]==',':
         percentage = response[:i]
         item =  response[i+2:]
         #print(percentage)
         
         return item 


def screenshots():
    while True:


        try:
            check, frame = webcam.read()
            print(check) #prints true as long as the webcam is running
            print(frame) #prints matrix values of each framecd
            cv2.imshow("Capturing", frame)
            key = cv2.waitKey(1)
            if key == ord('s'):
                cv2.imwrite(filename='saved_img.jpg', img=frame)
                # webcam.release()
                print("Processing image...")
                img_ = cv2.imread('saved_img.jpg', cv2.IMREAD_ANYCOLOR)
                # print("Converting RGB image to grayscale...")
                # gray = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)
                # print("Converted RGB image to grayscale...")
                # print("Resizing image to 28x28 scale...")
            # img_ = cv2.resize(gray,(28,28))
                # print("Resized...")
                # img_resized = cv2.imwrite(filename='saved_img-final.jpg', img=img_)
                print("Image saved!")
                
                html_content =f"""
                <!DOCTYPE html>
                <html>
                    <head>
                        <link rel="stylesheet" href="website.css">
                        
                    </head>
                    <body>
                        <div class="logo">
                <img src="askAI.jpg">
                        </div>
                        <div class="ChatGPTPrompt">
                            <p>Is it: {item}?
                            <hr class="under_line"/></p>
                        </div>




                        <div class="interactibles">
                                <button id="correct"><img src="car.png"></button>


                                <button id="incorrect"><img src="car.png"></button>


                        </div>

                        <button id="loadFileButton">Load response</button>
                <div id="ChatGPTPrompt" style="background-color: black; color:white;height:400px;"></div>

                      
                    </body>
                </html>

                """


                with open ('C:/Users/USERNAME/Python_workspace/ENproject/projectweb.html', 'w') as file:
                  file.write(html_content)

                print("done")
                # break
        
            elif key == ord('q'):
                webcam.release()
                cv2.destroyAllWindows()
                break
    
        except(KeyboardInterrupt):
            print("Turning off camera.")
            webcam.release()
            print("Camera off.")
            print("Program ended.")
            cv2.destroyAllWindows()
            break


        #image processing to get rid of unneccessary image data

# # print(topic)
   
response = confidence(encode_image)
print(response)    
item = percentage(response)

sleep(2)
screenshots() 
