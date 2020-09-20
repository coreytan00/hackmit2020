import uvicorn
from vidgear.gears.asyncio import WebGear

#various performance tweaks
options={"frame_size_reduction": 40, "frame_jpeg_quality": 80, "frame_jpeg_optimize": True, "frame_jpeg_progressive": False}

#initialize WebGear app  
web=WebGear(source=0, logging=True, **options)

#run this app on Uvicorn server at address http://localhost:8000/
uvicorn.run(web(), host='192.168.7.89', port=3000)

#close app safely
web.shutdown()