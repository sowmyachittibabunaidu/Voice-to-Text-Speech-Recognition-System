import tkinter as tk
from tkinter import messagebox
import speech_recognition as sr


class SpeechRecognitionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Speech Recognition System")
        self.root.geometry("760x560")
        self.root.minsize(700, 520)
        self.root.configure(bg="#f5f7fb")

        self.recognizer = sr.Recognizer()
        self.build_ui()

    def build_ui(self):
        tk.Label(
            self.root,
            text="Speech Recognition System",
            font=("Segoe UI", 24, "bold"),
            bg="#f5f7fb",
            fg="#172033",
        ).pack(pady=(28, 5))

        tk.Label(
            self.root,
            text="Convert your voice into text with one click.",
            font=("Segoe UI", 11),
            bg="#f5f7fb",
            fg="#657086",
        ).pack()

        card = tk.Frame(self.root, bg="white", highlightthickness=1,
                        highlightbackground="#e1e6ef")
        card.pack(fill="both", expand=True, padx=35, pady=25)

        self.text_box = tk.Text(
            card, height=17, wrap="word",
            font=("Segoe UI", 12),
            bg="#fbfcfe", fg="#172033",
            relief="flat", padx=15, pady=15
        )
        self.text_box.pack(fill="both", expand=True, padx=18, pady=18)

        buttons = tk.Frame(card, bg="white")
        buttons.pack(pady=(0, 15))

        tk.Button(
            buttons, text="🎤  Start Speaking",
            command=self.recognize_speech,
            font=("Segoe UI", 11, "bold"),
            bg="#2563eb", fg="white",
            activebackground="#1d4ed8", activeforeground="white",
            relief="flat", padx=18, pady=10, cursor="hand2"
        ).grid(row=0, column=0, padx=6)

        tk.Button(
            buttons, text="Clear",
            command=self.clear_text,
            font=("Segoe UI", 11),
            bg="#eef2f7", fg="#172033",
            relief="flat", padx=20, pady=10, cursor="hand2"
        ).grid(row=0, column=1, padx=6)

        tk.Button(
            buttons, text="Save Text",
            command=self.save_text,
            font=("Segoe UI", 11),
            bg="#eef2f7", fg="#172033",
            relief="flat", padx=20, pady=10, cursor="hand2"
        ).grid(row=0, column=2, padx=6)

        self.status = tk.Label(
            self.root,
            text="Ready — click Start Speaking.",
            font=("Segoe UI", 10),
            bg="#f5f7fb",
            fg="#657086",
        )
        self.status.pack(pady=(0, 20))

    def recognize_speech(self):
        try:
            with sr.Microphone() as source:
                self.status.config(text="Listening… speak clearly.")
                self.root.update_idletasks()
                self.recognizer.adjust_for_ambient_noise(source, duration=0.8)
                audio = self.recognizer.listen(source, timeout=8, phrase_time_limit=20)

            self.status.config(text="Processing speech…")
            self.root.update_idletasks()

            text = self.recognizer.recognize_google(audio)
            self.text_box.insert(tk.END, text + "\n")
            self.status.config(text="Speech recognized successfully.")

        except sr.WaitTimeoutError:
            self.status.config(text="No speech detected.")
            messagebox.showwarning("Timeout", "No speech was detected. Try again.")

        except sr.UnknownValueError:
            self.status.config(text="Could not understand the speech.")
            messagebox.showwarning(
                "Recognition Error",
                "The speech could not be understood. Please speak clearly and try again.",
            )

        except sr.RequestError:
            self.status.config(text="Speech service unavailable.")
            messagebox.showerror(
                "Connection Error",
                "The recognition service could not be reached. Check your internet connection.",
            )

        except OSError:
            self.status.config(text="Microphone unavailable.")
            messagebox.showerror(
                "Microphone Error",
                "No working microphone was found. Check your microphone permissions.",
            )

        except Exception as error:
            self.status.config(text="An unexpected error occurred.")
            messagebox.showerror("Error", str(error))

    def clear_text(self):
        self.text_box.delete("1.0", tk.END)
        self.status.config(text="Text cleared.")

    def save_text(self):
        text = self.text_box.get("1.0", tk.END).strip()

        if not text:
            messagebox.showwarning("Nothing to Save", "Recognize some speech before saving.")
            return

        with open("recognized_text.txt", "w", encoding="utf-8") as file:
            file.write(text)

        self.status.config(text="Text saved as recognized_text.txt.")
        messagebox.showinfo("Saved", "Recognized text saved successfully.")


if __name__ == "__main__":
    root = tk.Tk()
    SpeechRecognitionApp(root)
    root.mainloop()
