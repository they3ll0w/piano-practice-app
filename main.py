import tkinter as tk
from tkinter import ttk, font
import random
from typing import List, Tuple, Literal, Optional


class PianoPracticeApp:
    def __init__(self, root: tk.Tk) -> None:

        # Set up constants
        self.setup_constants()
        
        # Configure root window
        self.root = root
        self.root.title("Piano Practice Generator")
        self.root.geometry("500x300")
        self.root.configure(bg="#f0f0f0")
        
        # Create frame
        self.main_frame = ttk.Frame(root, padding=20)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Create title label
        title_font = font.Font(family="Arial", size=16, weight="bold")
        self.title_label = ttk.Label(
            self.main_frame, 
            text="Piano Practice Generator",
            font=title_font
        )
        self.title_label.pack(pady=(0, 20))
        
        # Create exercise display
        exercise_font = font.Font(family="Arial", size=14)
        self.exercise_label = ttk.Label(
            self.main_frame,
            font=exercise_font,
            wraplength=450
        )
        self.exercise_label.pack(pady=20)
        
        # Create button
        self.generate_button = ttk.Button(
            self.main_frame, 
            text="Generate New Exercise",
            command=self.generate_exercise,
            style="Accent.TButton"
        )
        self.generate_button.pack(pady=10)
        
        # Configure styles
        style = ttk.Style()
        style.configure("TFrame", background="#f0f0f0")
        style.configure("TLabel", background="#f0f0f0")
        style.configure("Accent.TButton", font=("Arial", 12))
        
        # Generate initial exercise
        self.generate_exercise()
        
    
    def setup_constants(self) -> None:

        # Major scales
        self.MAJOR_SHARP = ["C", "G", "D", "A", "E", "B", "F♯", "C♯"]
        self.MAJOR_FLAT = ["F", "B♭", "E♭", "A♭", "D♭", "G♭", "C♭"]
        self.MAJORS = [self.MAJOR_FLAT, self.MAJOR_SHARP]

        # Minor scales
        self.MINOR_SHARP = ["A", "E", "B", "F♯", "C♯", "G♯", "D♯"]
        self.MINOR_FLAT = ["D", "G", "C", "F", "B♭", "E♭", "A♭"]
        self.MINORS = [self.MINOR_FLAT, self.MINOR_SHARP]

        # Major tests
        self.MAJOR_SCALES = [
            "major", "separated by a third", "separated by a sixth", 
            "separated by a tenth", "contrary motion", "chromatic scale", "octaves"
        ]
        self.MAJOR_OCTAVES = ["four keys", "dominant seven chords", "dominant seven separated"]
        self.MAJOR_ARPEGGIO = [
            lambda: f"four key form {self.get_inversion(random.randint(0, 2))}",
            lambda: f"dominant seven {self.get_inversion(random.randint(0, 3))}"
        ]
        self.MAJOR_TESTS = [self.MAJOR_ARPEGGIO, self.MAJOR_OCTAVES, self.MAJOR_SCALES]

        # Minor tests
        self.MINOR_SCALES = ["harmonic", "melodic", "contrary motion"]
        self.MINOR_OCTAVES = ["four keys", "diminished seven chords", "diminished seven separated"]
        self.MINOR_ARPEGGIO = [
            lambda: f"four key form {self.get_inversion(random.randint(0, 2))}",
            lambda: f"diminished seven {self.get_inversion(random.randint(0, 3))}"
        ]
        self.MINOR_TESTS = [self.MINOR_ARPEGGIO, self.MINOR_SCALES, self.MINOR_OCTAVES]

        # Basic types
        self.MAJOR_MINOR: List[Literal["major", "minor"]] = ["major", "minor"]
    
    def get_inversion(self, inv: int) -> str:
        inversions = {
            0: "first inversion",
            1: "second inversion",
            2: "third inversion",
            3: "fourth inversion"
        }
        return inversions.get(inv, "root position")
    
    def choose_major_or_minor(self) -> Literal["major", "minor"]:
        return random.choice(self.MAJOR_MINOR)
    
    def choose_key(self, major_or_minor: Literal["major", "minor"]) -> str:
        if major_or_minor == "major":
            f_or_s = random.choice(self.MAJORS)
            return random.choice(f_or_s)
        else:
            f_or_s = random.choice(self.MINORS)
            return random.choice(f_or_s)
    
    def choose_test(self, major_or_minor: Literal["major", "minor"]) -> str:
        test_list = self.MINOR_TESTS if major_or_minor == "minor" else self.MAJOR_TESTS
        
        test_category = random.choice(test_list)
        test = random.choice(test_category)
        
        # Handle lambda functions for dynamic text
        if callable(test):
            return test()
        return test
    
    def generate_exercise(self) -> None:
        major_or_minor = self.choose_major_or_minor()
        key = self.choose_key(major_or_minor)
        test = self.choose_test(major_or_minor)
        
        exercise_text = f"Perform {key} {major_or_minor}, in {test}"
        self.exercise_label.config(text=exercise_text)


if __name__ == "__main__":
    root = tk.Tk()
    app = PianoPracticeApp(root)
    root.mainloop()
