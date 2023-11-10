from pytube import Playlist
from moviepy.editor import *
import os

def download_videos_and_convert_to_wav(playlist_url, output_path):
    # Create a playlist object
    p = Playlist(playlist_url)
    
    # Initialize a counter for naming files
    track_number = 1
    
    # Loop through all videos in the playlist
    for video in p.videos:
        try:
            # Get the highest resolution video stream available
            video_stream = video.streams.get_highest_resolution()
            
            # Download the video stream
            video_file_path = video_stream.download(output_path=output_path)
            
            # Load the video file
            video_clip = VideoFileClip(video_file_path)
            
            # Extract audio from video
            audio_clip = video_clip.audio
            
            # Format the new filename
            audio_file_path = os.path.join(output_path, f"classical_{track_number}.wav")
            
            # Save the audio file
            audio_clip.write_audiofile(audio_file_path)
            
            # Increment the track counter
            track_number += 1
            
            # Print success message
            print(f"Downloaded and converted video to WAV: {audio_file_path}")
        except Exception as e:
            # Print the error
            print(f"An error occurred with track {track_number}: {e}")
        finally:
            # Always close the clips if they were created
            if 'video_clip' in locals():
                video_clip.close()
            if 'audio_clip' in locals():
                audio_clip.close()
            
            # Delete the original video file if it exists
            if os.path.exists(video_file_path):
                os.remove(video_file_path)
                print(f"Deleted the original video file: {video_file_path}")

# Use the function with your playlist URL
playlist_url = 'https://www.youtube.com/playlist?list=PLW9Nl3YHfwUpgh1GCoh2qPrzwzGDLQ6UF'
download_videos_and_convert_to_wav(playlist_url, output_path='Audio_Processing/yt_playlist_downloaded/')
