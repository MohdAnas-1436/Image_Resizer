import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, UnidentifiedImageError

class ImageResizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Batch Image Resizer")
        self.root.geometry("550x200")

        # --- File selection ---
        tk.Label(root, text="Selected Images:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.files_entry = tk.Entry(root, width=50)
        self.files_entry.grid(row=0, column=1, padx=10)
        tk.Button(root, text="Browse", command=self.select_files).grid(row=0, column=2, padx=10)

        # --- Width and Height ---
        tk.Label(root, text="Width:").grid(row=1, column=0, padx=10, sticky="e")
        self.width_entry = tk.Entry(root, width=10)
        self.width_entry.grid(row=1, column=1, sticky="w")
        self.width_entry.insert(0, "800")

        tk.Label(root, text="Height:").grid(row=1, column=1, sticky="e", padx=(0, 60))
        self.height_entry = tk.Entry(root, width=10)
        self.height_entry.grid(row=1, column=2, sticky="w")
        self.height_entry.insert(0, "600")

        # --- Format ---
        tk.Label(root, text="Format:").grid(row=2, column=0, padx=10, sticky="w")
        self.format_var = tk.StringVar(value="JPEG")
        tk.OptionMenu(root, self.format_var, "JPEG", "PNG", "WEBP", "BMP").grid(row=2, column=1, sticky="w")

        # --- Resize button ---
        tk.Button(root, text="Resize Images", command=self.resize_images).grid(row=3, column=1, pady=15)

    def select_files(self):
        files = filedialog.askopenfilenames(
            title="Select Image Files",
            filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp *.gif *.webp *.tiff")]
        )
        if files:
            self.files_entry.delete(0, tk.END)
            self.files_entry.insert(0, "|".join(files))  # Use "|" as separator for file paths

    def resize_images(self):
        # Read and split file paths
        file_paths_raw = self.files_entry.get().strip()
        if not file_paths_raw:
            messagebox.showerror("Error", "No images selected.")
            return

        file_paths = file_paths_raw.split("|")
        valid_images = []

        for path in file_paths:
            try:
                with Image.open(path) as img:
                    valid_images.append(path)
            except UnidentifiedImageError:
                print(f"Skipped (not an image): {path}")
            except Exception as e:
                print(f"Skipped (error): {path} — {e}")

        if not valid_images:
            messagebox.showerror("Error", "No valid image files selected.")
            return

        # Get resize dimensions and format
        try:
            width = int(self.width_entry.get())
            height = int(self.height_entry.get())
            output_format = self.format_var.get()
        except ValueError:
            messagebox.showerror("Error", "Width and height must be integers.")
            return

        # Prepare output directory
        output_dir = os.path.join(os.path.dirname(valid_images[0]), "resized_output")
        os.makedirs(output_dir, exist_ok=True)

        resized_count = 0
        for path in valid_images:
            try:
                with Image.open(path) as img:
                    resized = img.resize((width, height), Image.LANCZOS)
                    base = os.path.splitext(os.path.basename(path))[0]
                    output_path = os.path.join(output_dir, f"{base}.{output_format.lower()}")
                    resized.convert("RGB").save(output_path, output_format)
                    resized_count += 1
            except Exception as e:
                print(f"Failed to resize {path}: {e}")

        if resized_count == 0:
            messagebox.showwarning("Warning", "Images found, but none were successfully resized.")
        else:
            messagebox.showinfo("Success", f"Resized {resized_count} image(s) and saved to:\n{output_dir}")


if __name__ == "__main__":
    root = tk.Tk()
    app = ImageResizerApp(root)
    root.mainloop()
