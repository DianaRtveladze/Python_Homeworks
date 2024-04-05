import requests
import threading


def download_mp3(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(response.content)
    print(f"Downloaded {filename}")


def main():
    urls = [
        "https://example.com/song1.mp3",
        "https://example.com/song2.mp3",
        "https://example.com/song3.mp3",
        # Add more URLs here
    ]

    threads = []
    for i, url in enumerate(urls):
        filename = f"song{i + 1}.mp3"
        t = threading.Thread(target=download_mp3, args=(url, filename))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    print("All downloads are finished.")


if __name__ == "__main__":
    main()
