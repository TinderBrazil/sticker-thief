class Strings:
    START_MESSAGE = ("Olá,\n"
                     "Você pode me usar para criar pacotes de adesivos personalizados usando adesivos existentes ou arquivos PNG.\n"
                     "\n"
                     "Principais comandos:\n"
                     "/create para criar um novo pacote\n"
                     "/createanimated para criar um novo pacote animado\n"
                     "/add para adicionar adesivos a um pacote existente\n"
                     "/help para mais comandos")

    HELP_MESSAGE = ("<b>Lista completa de comandos</b>:\n"
                    "- /create: criar um novo pacote\n"
                    "- /createanimated para criar um novo pacote animado\n"
                    "- /add: adicionar um adesivo a um pacote\n"
                    "- /remove: remover um adesivo de seu pacote\n"
                    "- me envie um adesivo e eu vou enviar-lhe o seu png de volta\n"
                    "- /list: liste seus pacotes (máximo 100 entradas)\n"
                    "- /export: exportar um pacote de adesivos como um zip de arquivos png\n"
                    "- /forgetme: excluir-se do meu banco de dados. Os pacotes que você criou <b>não</b> serão excluídos do Telegram\n"
                    "- /cleanup: remover da lista de seus pacotes todos os pacotes que você excluiu usando @stickers\n"
                    "\n"
                    "<b>Outras operações</b>\n"
                    "Você pode excluir um pacote, alterar os emojis de um adesivo, alterar a ordem dos adesivos e ver as estatísticas de um adesivo/pacote de @stickers\n"
                    "\n"
                    "<b>Dicas</b>:\n"
                    "- ao adicionar um adesivo ou criar um pacote, você pode passar um adesivo ou um arquivo png\n"
                    "- ao adicionar um adesivo como png, você pode passar seus emojis na legenda\n"
                    "\n"
                    "<b>Outras informações</b>\n"
                    "Todos os pacotes que você cria comigo têm seus links terminando por \"_by_{}\". Isso não é feito de propósito., "
                    "mas algo forçado pelo Telegram\n"
                    "\n"
                    "<b>Maneira correta de construir seu próprio pacote personalizado</b>\n"
                    "Usar @Obikyu. Não rouba adesivos como eu. Está queimando rápido também. Realmente sugerido")

    PACK_CREATION_STATIC_WAITING_TITLE = ("Tudo bem, um novo pacote de adesivos! Por favor, me envie o título do pacote. "
                                          "(não deve exceder 64 caracteres).\n"
                                          "Usar /cancel para cancelar")

    PACK_CREATION_ANIMATED_WAITING_TITLE = ("Tudo bem, um novo pacote animado! Por favor, me envie o título do pacote. "
                                            "(não deve exceder 64 caracteres).\n"
                                            "Usar /cancel para cancelar")

    PACK_TITLE_TOO_LONG = "Desculpe, o título deve ter no máximo 64 caracteres. Tente com outro título"

    PACK_TITLE_CONTAINS_NEWLINES = "Sinto muito, o título deve ser uma única linha (sem personagens newline)"

    PACK_CREATION_WAITING_NAME = ("Bom, este vai ser o título do pacote: <i>{}</i>\n"
                                  "\n"
                                  "Por favor, envie-me o que será o link pacote (deve estar no máximo {} personagens longo. "
                                  "<b>Não</b> precisa incluir <code>https://t.me/addstickers/</code>)")

    PACK_NAME_TOO_LONG = "Desculpe, este link é muito longo ({}/{}). Tente novamente com outro link"

    PACK_NAME_INVALID = ("<b>Link inválido</b>. Um link deve:\n"
                         "• começar com uma carta\n"
                         "• consistem exclusivamente de letras, dígitos ou sublinhados\n"
                         "• não contêm dois sublinhados consecutivos\n"
                         "• não terminar com um sublinhado\n"
                         "\n"
                         "Por favor, tente de novo.")

    PACK_NAME_DUPLICATE = "Sinto muito, você já tem um pacote com este link salvo. tentar com outro link"

    PACK_CREATION_WAITING_FIRST_STATIC_STICKER = "Entendi, estamos quase terminando. Agora me mande o primeiro adesivo " \
                                                 "do pacote (ou um arquivo png)"

    PACK_CREATION_WAITING_FIRST_ANIMATED_STICKER = "Entendi, estamos quase terminando. Agora me envie o primeiro adesivo animado " \
                                                   "do pacote"

    PACK_CREATION_FIRST_STICKER_PACK_DATA_MISSING = ("Ooops, algo deu errado..\n"
                                                     "Por favor, repita o processo de criação com /create")

    PACK_CREATION_ERROR_DUPLICATE_NAME = ("Desculpe, já tem um bando com. <a href=\"{}\">este link</a>.\n"
                                          "Por favor, me envie um novo link, ou /cancel")

    PACK_CREATION_ERROR_INVALID_NAME = ("Sinto muito, telegrama rejeitou o link que você forneceu dizendo que não é válido.\n"
                                        "Por favor, envie um novo link para mim, ou /cancel")

    PACK_CREATION_ERROR_GENERIC = ("Erro ao tentar criar o pacote: <code>{}</code>.\n"
                                   "Por favor, tente de novo, ou. /cancel")

    PACK_CREATION_PACK_CREATED = ("Seu pacote foi criado, adicioná-lo através <a href=\"{}\">este link</a>\n"
                                  "Continue me mandandando adesivos para adicionar mais, ou /done")

    ADD_STICKER_SELECT_PACK = "Selecione o pacote ao que deseja adicionar adesivos, ou /cancel"

    ADD_STICKER_NO_PACKS = "Você não tem nenhum pacote ainda. Usar /create para começar a criar um novo pacote"

    ADD_STICKER_SELECTED_TITLE_DOESNT_EXIST = ("Parece que o bando \"{}\" não existe.\n"
                                               "Selecione um pacote válido no teclado")

    ADD_STICKER_SELECTED_TITLE_MULTIPLE = ("Parece que você tem vários pacotes que combinam com o título \"{}\".\n"
                                           "Selecione o pacote que deseja escolher no teclado abaixo. Referência de pacotes:\n"
                                           "• {}")

    ADD_STICKER_PACK_SELECTED_STATIC = ("Bom, vamos adicionar adesivos para <a href=\"{}\">este pacote</a>.\n"
                                        "Envie-me um adesivo ou um arquivo png")

    ADD_STICKER_PACK_SELECTED_ANIMATED = ("Bom, vamos adicionar adesivos para <a href=\"{}\">este pacote</a>.\n"
                                          "Mande-me um adesivo animado")

    ADD_STICKER_SELECTED_NAME_DOESNT_EXIST = ("Parece que o bando \"{}\" não existe.\n"
                                              "Selecione um pacote válido no teclado")

    ADD_STICKER_PACK_DATA_MISSING = ("Ooops, algo deu errado.\n"
                                     "Por favor, repita o processo com /add")

    ADD_STICKER_PACK_NOT_VALID = ("Ooops, parece que <a href=\"{}\">este pacote</a> não existe.\n"
                                  "Por favor, selecione outro pacote")

    ADD_STICKER_PACK_NOT_VALID_NO_PACKS = ("Ooops, parece que <a href=\"{}\">este pacote</a> não existe.\n"
                                           "Por favor, crie um novo pacote com /create")

    ADD_STICKER_SUCCESS = ("Adesivo adicionado a <a href=\"{}\">este pacote</a>. "
                           "Continue me mandandando adesivos para adicionar mais, usar /done quando você está feito")

    ADD_STICKER_PACK_FULL = ("Desculpa, <a href=\"{}\">este pacote</a> está cheio ({} stickers), "
                             "você não pode mais adicionar adesivos a ele. Use /remove para remover alguns adesivos\n"
                             "Você saiu do modo \ adicionando adesivos.")

    ADD_STICKER_SIZE_ERROR = ("Parece que um erro aconteceu ao redimensionar o adesivo. "
                              "e agora suas dimensões são {}x{} px. I não pode adicionar este adesivo ao pacote devido à lógica de redimensionamento errada.\n"
                              "Envie-me outro adesivo, ou use /done quando você está feito")

    ADD_STICKER_INVALID_ANIMATED = ("Parece que este adesivo não é compatível com o mais recente "
                                    "<a href=\"https://core.telegram.org/animated_stickers\">Telegram guidelines</a> "
                                    "sobre adesivos animados. Sinto muito, mas não posso acrescentar. :(\n"
                                    "Você pode tentar enviar o adesivo novamente or "
                                    "enviar outro adesivo animado (or /cancel)")

    ADD_STICKER_GENERIC_ERROR = ("Um erro ocorreu ao adicionar este adesivo a <a href=\"{}\">este pacote</a>: "
                                 "<code>{}</code>.\n"
                                 "Tente de novo, me envie outro adesivo ou use /done when você está feito")

    ADD_STICKER_ANIMATED_UNSUPPORTED = ("Sinto muito, eu não suportei adesivos animados ainda :(\n"
                                        "Por favor, envie um adesivo estático")

    ADD_STICKER_EXPECTING_STATIC = ("Não, não, não, não. Eu estava esperando por um adesivo normal, não um animado. "
                                    "Por favor, me envie um adesivo estático, ou /cancel")

    ADD_STICKER_EXPECTING_ANIMATED= ("Não, não, não, não. Eu estava esperando por um adesivo animado, não um normal. "
                                     "Por favor, me envie um adesivo animado, ou /cancel")

    REMOVE_STICKER_SELECT_STICKER = "Envie-me o adesivo que você quer remover de sua embalagem, ou /cancel"

    REMOVE_STICKER_SUCCESS = ("Adesivo removido de <a href=\"{}\">seu pacote</a>.\n"
                              "Envie-me outro adesivo para remover, ou /done quando você're Feito")

    REMOVE_STICKER_FOREIGN_PACK = ("Este adesivo é de um <a href=\"{}\">Pack</a> você não criou através de mim. "
                                   "Tente com um adesivo válido, ou /done")

    REMOVE_STICKER_ALREADY_DELETED = ("Este adesivo não faz mais parte <a href=\"{}\">o pacote</a>, "
                                      "tentar com outro adesivo")

    REMOVE_STICKER_GENERIC_ERROR = (
        "Ocorreu um erro ao remover este adesivo de <a href=\"{}\">este pacote</a>: "
        "<code>{}</code>.\n"
        "Tente de novo, me envie outro adesivo ou use /done quando você está feito")

    FORGETME_SUCCESS = "Sucesso, eu excluí todos os seus pacotes do meu banco de dados"

    CANCEL = "Bom, acabamos com isso."

    LIST_NO_PACKS = "Você não tem nenhum pacote. Usar /create para criar um"

    LIST_FOOTER = "\n\n<b>s</b>: Estático\n<b>a</b>: Animado"

    ANIMATED_STICKERS_NO_FILE = "Oh não, eu não posso enviar-lhe adesivos animados de volta como arquivo!"

    EXPORT_PACK_SELECT = "Por favor, envie-me um stciker do pacote que você quer exportar, ou /cancel"

    EXPORT_PACK_NO_PACK = "Este adesivo não pertence a nenhum pacote. Por favor, envie-me um stciker de um pacote, ou /cancel"

    EXPORT_PACK_START = "Exportando adesivos de <i>{}</i>... iT pode levar alguns minutos. Por favor, espere."

    EXPORT_PACK_UPLOADING = "Zipping arquivos png e upload..."

    EXPORT_ANIMATED_STICKERS_NOT_SUPPORTED = "A exportação de pacotes animados ainda não é suportada"

    CLEANUP_NO_PACK = ("Parece que todas as suas mochilas ainda estão lá. Nenhum pacote foi removido do banco de dados.\n"
                       "Usar /list para ver a lista de seus pacotes")

    CLEANUP_HEADER = "Estes são os pacotes que não existem mais e foram removidos do banco de dados:\n"
