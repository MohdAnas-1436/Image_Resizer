# 🖼️ GUI Batch Image Resizer Tool

A simple and powerful **desktop app** built with Python that allows you to **resize and convert multiple image files** at once using a graphical user interface (GUI). Perfect for designers, developers, and photographers who need to batch-process images with ease.

---

## 🚀 Features

* ✅ Select multiple image files (JPG, PNG, BMP, etc.)
* 📏 Resize all images to a custom width and height
* 🌀 Convert images to popular formats: **JPEG**, **PNG**, **WEBP**, **BMP**
* 📁 Automatically saves resized images to a `resized_output/` folder
* 🧠 Built with **Python**, **Tkinter**, and **Pillow**
* 💡 Beginner-friendly and easy to extend

---

## 🛠️ Requirements

Make sure you have Python installed. Then install the required library:

```bash
pip install pillow
```

---

## 🧑‍💻 How to Run

1. **Download or clone** this repository.
2. Save the code as `gui_image_resizer.py`.
3. Open a terminal and run:

```bash
python gui_image_resizer.py
```

---

## ✨ Usage Instructions

1. Click **"Browse"** to select one or more image files.
2. Enter the desired **Width** and **Height** in pixels.
3. Choose the output **Format** (JPEG, PNG, etc.).
4. Click **"Resize Images"**.
5. The resized images will be saved in a folder named `resized_output` inside the location of the first selected image.

---

## 📸 Supported Image Formats

* `.jpg`
* `.jpeg`
* `.png`
* `.webp`
* `.bmp`
* `.gif`
* `.tiff`

---

## 📂 Output Folder Structure

Example:

```
📁 your_images/
├── img1.jpg
├── img2.png
├── ...
└── 📁 resized_output/
    ├── img1.jpeg
    ├── img2.jpeg
```

---

## 🧩 Want More Features?

Planned features:

* [ ] Drag & drop support
* [ ] Resize by percentage
* [ ] Image preview
* [ ] Folder selection mode
* [ ] `.exe` Windows standalone app

Open an issue or suggest a feature! 👇

---

## 🧠 Built With

* [Python](https://www.python.org/)
* [Tkinter](https://docs.python.org/3/library/tkinter.html)
* [Pillow](https://python-pillow.org/)

---
