MESAJ="GoldUserBot Aftomatik Deploy Qurulumuna Xoş Gəldiniz"
MESAJ+="\nTelegram: @AsenaUserBot"
echo y | apk update
clear
echo -e $MESAJ
echo "Python Yüklənir"
echo y | apk add python3
clear
echo -e $MESAJ
echo "Git Yüklənir"
echo y | apk add git
clear
echo -e $MESAJ
echo "TeleThon Yüklənir"
python3 -m pip install telethon
echo "Repo klonlanır..."
git clone https://github.com/Emin-ahmedoff/goldeninstaller
clear
echo -e $MESAJ
clear
echo -e $MESAJ
echo "Bəzi altyapı Fayılları Yüklənir"
cd Installer
python3 -m pip install wheel
python3 -m pip install -r requirements.txt
clear
python3 -m golden_installer