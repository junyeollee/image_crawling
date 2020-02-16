from google_images_download import google_images_download  # importing the library


KEYWORDS = ["smartphone is comming"]


def get_img_from_google(keywords):
    response = google_images_download.googleimagesdownload()  # class instantiation

    arguments = {"keywords": keywords, "limit": 10,
                 "print_urls": True, "format": "jpg"}  # creating list of arguments
    # passing the arguments to the function
    paths = response.download(arguments)
    print(paths)  # printing absolute paths of the downloaded images


def main(keywords):
    for k in keywords:
        get_img_from_google(k)


if __name__ == "__main__":
    main(KEYWORDS)
