MESAJ="GoldenUserBot Aftomatik Deploy Quruluma Xoş Gəldiniz"
MESAJ+="\nTelegram: @GoldenUserBot"
pkg update -y
clear
echo -e $MESAJ
echo "Python Yüklənir"
pkg install python -y
clear
echo -e $MESAJ
echo "Git Yüklənir"
pkg install git -y
clear
echo -e $MESAJ
echo "TeleThon Yüklənir"
pip install telethon
echo "Repo Klonlanır..."
git clone https://github.com/Emin-ahmedoff/goldeninstaller
clear
echo -e $MESAJ
cd goldeninstaller
clear
echo "Bəzi Alt Yapı faylları yüklənir"
echo -e $MESAJ
pip install wheel
pip install -r requirements.txt
python -m golden_installer
