"""
Módulo responsável pelo carregamento e sobreposição dos emojis nos frames de vídeo.
"""


class EmojiOverlay:
    """
    Classe para carregar imagens de emojis e sobrepor na imagem/vídeo.
    """

    def __init__(self, emojis_dir="assets/emojis"):
        # TODO: Carregar dicionário de imagens de emojis pré-carregados
        pass

    def apply_overlay(self, frame, emotion, bbox=None):
        """
        Sobrepõe o emoji correspondente à emoção detectada no frame (ex: sobre o rosto ou em um canto do vídeo).
        """
        # TODO: Redimensionar e aplicar sobreposição respeitando transparência (canal alfa)
        pass
