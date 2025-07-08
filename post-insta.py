from instagrapi import Client

def post_to_instagram(username, password, image_path, caption):
    try:
        cl = Client()
        cl.login(username, password)
        cl.photo_upload(image_path, caption)
        print("Instagram post uploaded successfully!")
    except Exception as e:
        print(f"Error posting to Instagram: {e}")

if __name__ == "__main__":
    instagram_username = "temp_account_lw"
    instagram_password = "dipseek"
    instagram_image_path = "C:/DIPSEEK/LnB/summer internship program 2025/python_tasks/url_tasks/20250615_OHR.SeaTurtleBrazil_EN-IN8664549604_UHD_bing.jpg"
    instagram_caption = "Posted via Python! #Automation"
    post_to_instagram(instagram_username, instagram_password, instagram_image_path, instagram_caption)