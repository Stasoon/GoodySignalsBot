from aiogram.utils.markdown import quote_html

from config import Config


class Messages:
    #  Статья с фото: https://telegra.ph/Goody-signals-photos-07-03

    @staticmethod
    def get_welcome(user_name: str = 'незнакомец') -> str:
        return (
            "🤖 You can get a BOT and start earning money completely free!"
        )

    @staticmethod
    def get_welcome_photo() -> str:
        return 'https://telegra.ph/file/90cfc683f8c5e75e9b34b.png'

    @staticmethod
    def __get_registration_steps():
        return (
            'To get the bot free for 3 days, you need: \n\n'

            '1. Click on the <b>«REGISTRATION»</b> button and register on the 1WIN \n\n'

            '2. After that, click on <b>«CONFIRM REGISTRATION»</b> \n\n'

            '3. After successful registration the bot is activated \n\n'

            '<i>❗To successfully register, you must register a new account, because the '
            'algorithms do not work with old accounts</i>'
        )

    @staticmethod
    def get_registration():
        return (
            '✅ You need to activate the bot \n\n'
            f'{Messages.__get_registration_steps()}'
        )

    @staticmethod
    def get_registration_photo():
        return 'https://telegra.ph/file/1ccf3adf7f828b66ab38d.png'

    @staticmethod
    def get_registration_passed():
        return (
            '✅ Bot activated successfully \n\n'

            '<i>Click the button and start earning!</i> ⤵️'
        )

    @staticmethod
    def get_registration_not_passed():
        return (
            f'❌ REGISTRATION FAILED! ❌ \n'
            'Read the rules carefully! \n\n'

            f'{Messages.__get_registration_steps()}'
        )

    @staticmethod
    def get_registration_not_passed_photo() -> str:
        return 'https://telegra.ph/file/3a5bd7e371b1c6578fa5f.png'

    # @staticmethod
    # def get_deposit_not_found():
    #     return '❗️Your deposit was not found, please try again.'
    #
    # @staticmethod
    # def get_bot_activated():
    #     private_channel_link = 'https://t.me/+H4zf0sONYL0wNmUy'
    #     return (
    #         '✅ <b>BOT ACTIVATED</b>⭐️ \n\n'
    #
    #         'Click the <b>SIGNALS</b> button and start earning money! \n\n'
    #
    #         'A private channel is available to you, stay tuned for updates to the bot! \n'
    #         f'➡️ {private_channel_link} \n<b>(subscribe)</b>'
    #     )

    @staticmethod
    def get_bot_activated_photo():
        return 'https://telegra.ph/file/d2dab3354fd7870ba75dd.png'
