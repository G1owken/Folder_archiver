from tkinter import filedialog, Tk, messagebox
from password_gen import generate_random_password
from archiver import create_protected_archive
from decoder import decrypt_and_extract

def main():
    root = Tk()
    root.withdraw()
    root.attributes('-topmost', True)

    # Выбор режима
    choice = messagebox.askyesnocancel("Brute_forcer", "ДА — Зашифровать папку\nНЕТ — Расшифровать архив")

    if choice is True: # ШИФРОВАНИЕ
        path = filedialog.askdirectory(title="Выберите папку для защиты")
        if not path: return
        
        # Спрашиваем только подтверждение на удаление
        if messagebox.askyesno("Удаление", f"Папка {path} будет удалена. Продолжить?"):
            pwd = generate_random_password(24)
            # Вызываем архиватор (он сам положит всё в нужные папки)
            arc_p, key_p = create_protected_archive(path, pwd)
            messagebox.showinfo("Успех", f"Зашифровано!\nАрхив в папке 'archives'\nКлюч в папке 'passwords'")

    elif choice is False: # РАСШИФРОВКА
        # Выбираем архив из папки archives
        arc = filedialog.askopenfilename(title="Выбери архив", filetypes=[("7z files", "*.7z")])
        if not arc: return
        
        # Выбираем ключ из папки passwords
        key = filedialog.askopenfilename(title="Выбери ключ", filetypes=[("Text files", "*.txt")])
        if not key: return
        
        # Куда вернуть папку
        out = filedialog.askdirectory(title="Куда распаковать?")
        
        if out:
            try:
                decrypt_and_extract(arc, key, out)
                messagebox.showinfo("Готово", "Папка успешно восстановлена!")
            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось: {e}")

if __name__ == "__main__":
    main()