# Taking Screenshots using pyscreenshot
import pyscreenshot

# Run from terminal
if __name__ == "__main__":
    # Capture the screen
    img = pyscreenshot.grab()
    # Show  the screenshot
    img.show()
    # Save the captured screenshot
    img.save('screenshot.png')
    print("Done!, Screenshot saved")

