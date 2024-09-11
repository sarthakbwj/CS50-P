import re

def main():
    # Get the HTML input from the user
    print(parse(input("HTML: ")))

def parse(s):
    # Regular expression to capture YouTube embed links from iframe src attribute
    match = re.search(r'src="https?://(?:www\.)?youtube\.com/embed/(\w+)"', s)
    
    if match:
        # Extract the video ID from the match
        video_id = match.group(1)
        # Return the shorter youtu.be URL
        return f"https://youtu.be/{video_id}"
    
    # If no match is found, return None
    return None

if __name__ == "__main__":
    main()
