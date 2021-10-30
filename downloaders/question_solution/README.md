# Prerequisites
1. `video_id` this is required to get the target video.
2. Video url format `https://player.vimeo.com/video/{ VIMEO_VIDEO_ID }`
3. `referer` header this is required by vimeo to allow access to private videos. I am using `https://www.algoexpert.io` cause all videos are allowed in `https://www.algoexpert.io` origin.
4. Add below headers to change if need arises.

Example of Headers for every requests sent to the Vimeo backend:
```json
{
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9,bn;q=0.8",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Host": "player.vimeo.com",
    "Pragma": "no-cache",
    "Referer": "https://www.algoexpert.io/",
    "sec-ch-ua": "\"Google Chrome\";v=\"95\", \"Chromium\";v=\"95\", \";Not A Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Windows",
    "Sec-Fetch-Dest": "iframe",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36",
}
```
