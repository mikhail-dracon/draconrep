Как создать ключ

Давайте создадим наш первый ключ при помощи команды:
ssh-keygen -t ed25519 -C "имя.фамилия@phystech.edu"
Где ed25519 это просто формат ключа, а после ключа -C идёт ваш email.
Программа предложит вам переименовать ключ, можно отказаться (его можно переименовать позже)и попросит ввести пароль для ключа
(его можно оставить пустым). Теперь если вы еще раз выполнить команду ls ~/.ssh, то должны увидеть там два файла id_ed25519 и 
id_ed25519.pub. Это просто текстовое представление некоторого очень большого числа. Вывести значение ключа на экран можно при 
помощи команды:
cat ~/.ssh/id_ed25519.pub

Как добавить ключ в аакаунт на GitHub

Для этого наведите на вашу иконку в правом верхнем углу, выберите пункт Settings, найдите слева пункт SSH and GPG keys, нажмите
на кнопку New SSH key.
Откроется окно, в котором можно ввести название в поле Title. В поле Key нужно вставить публичный ключ. Его можно получить при 
помощи команды на вашем компьютере cat ~/.ssh/id_ed25519.pub. Скопируйте ключ из терминала, и вставьте его, после чего нажмите 
Add SSH key.

Как склонировать репозиторий

Если вы находитесь в папке с другим репозиторием, то выйдите из нее. Не стоит клонировать репозиторий в другой репозиторий!
Теперь необходимо получить созданный репозиторий. Это можно сделать при помощи команды, где в <url> вставьте адрес репозитория:
git clone <url>
После этого в текущей папке появится папка с названием вашего репозитория. Отлично!



