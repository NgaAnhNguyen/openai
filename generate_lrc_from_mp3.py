import whisper
import os

def seconds_to_timestamp(seconds):
    """
    Chuyển đổi số giây thành định dạng timestamp LRC: mm:ss.xx
    """
    minutes = int(seconds // 60)
    secs = seconds % 60
    return f"{minutes:02d}:{secs:05.2f}"

def generate_lrc(audio_file, output_lrc):
    # Load model Whisper (ở đây sử dụng model "base", bạn có thể chọn model khác)
    model = whisper.load_model("base")
    
    # Transcribe file audio, kết quả là một dictionary có các segment
    result = model.transcribe(audio_file)
    
    # Mở file LRC để ghi kết quả
    with open(output_lrc, "w", encoding="utf-8") as f:
        for segment in result["segments"]:
            timestamp = seconds_to_timestamp(segment["start"])
            text = segment["text"].strip()
            # Ghi mỗi dòng theo định dạng [mm:ss.xx] Lời bài hát
            f.write(f"[{timestamp}] {text}\n")
    
    print(f"File LRC đã được tạo: {output_lrc}")

if __name__ == "__main__":
    # Đường dẫn file audio cần chuyển đổi (sử dụng raw string để tránh lỗi escape)
    audio_file = r"C:\Users\NITRO 5\Downloads\ROSÉ - APT..mp3"
    output_lrc = "output.lrc"
    
    if not os.path.exists(audio_file):
        print(f"Không tìm thấy file {audio_file}")
    else:
        generate_lrc(audio_file, output_lrc)
