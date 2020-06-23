Adesivos ladrão bot
Eu fiz esse bot porque estava exausto de perder meu tempo procurando aquele adesivo perfeito para usar entre todos os meus pacotes instalados.

Recursos:

crie pacotes de adesivos estáticos e animados
adicione adesivos a um pacote existente apenas enviando outros adesivos (arquivos png também são aceitos)
redimensione automaticamente os arquivos png para que eles atendam aos requisitos de tamanho do telegrama
remover adesivos de um pacote
converter adesivos em arquivos png (e redimensioná-los se forem muito grandes)
exportar um pacote de adesivos como um zip de arquivos png
aviso Legal
Usar esse tipo de bots é uma solução horrível. Você está retirando o conteúdo da comunidade criado por outros usuários para anonimá-lo, incluindo-o em seus pacotes personalizados. Isso reforça fortemente o compartilhamento de boas embalagens - e às vezes a apropriação de adesivos também pode cair em violação de direitos autorais.

Se você respeita o trabalho de outras pessoas, deseja dar créditos aos criadores do pacote original e compartilhar os pacotes dos quais você tirou seus adesivos favoritos, use @MyPackBot . Posso garantir que esse bot é ótimo

Executando o bot
instalar requisitos com pip3 install -r requirements.txt
renomear config.example.tomla config.tomle alterar valores relevantes (isto é, telegram.tokene telegram.admins)
execute o bot com python3 main.py
Notas para quem vai executar isso
Este bot não foi criado para ser usado por uma grande quantidade de usuários e não posso garantir seu desempenho.

Por padrão, todos podem usar este bot (com exceção de alguns comandos especiais, listados abaixo). Se você deseja restringir seu uso apenas aos usuários listados em telegram.admins( condfig.tomlarquivo), abra config.tomle alteretelegram.admins_only para true.

Ao usar o git, certifique-se de executar o alembic para atualizar seu esquema do banco de dados: alembic upgrade head

Quando você puxa o git, consegue executar o alambique para atualizar seu esquema do banco de dados: alembic upgrade headO que outras pessoas estão dizendo
