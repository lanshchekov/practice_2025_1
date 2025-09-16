import hashlib as hasher
import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QLabel
)


class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hasher.sha256()
        # Create encoded string as a hash body
        hash_body = (str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)).encode()
        sha.update(hash_body)
        return sha.hexdigest()


import datetime as date


def create_genesis_block():
    # Manually construct a block with
    # index zero and arbitrary previous hash
    return Block(0, date.datetime.now(), "Genesis Block", "0")


def next_block(last_block, data):
  index = last_block.index + 1
  timestamp = date.datetime.now()
  return Block(index, timestamp, data, last_block.hash)


class BlockchainApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Блокчейн")
        self.resize(800, 600)

        # Инициализация блокчейна
        self.blockchain = [create_genesis_block()]
        self.last_block = self.blockchain[0]

        # Элементы интерфейса
        layout = QVBoxLayout()

        self.label = QLabel("Демонстрация работы блокчейна")
        self.label.setFont(QFont('Arial', 11))
        layout.addWidget(self.label)

        self.text_output = QTextEdit()
        self.text_output.setFont(QFont('Arial', 11))
        self.text_output.setReadOnly(True)
        layout.addWidget(self.text_output)

        self.add_button = QPushButton("Добавить новый блок")
        self.add_button.setFont(QFont('Arial', 11))
        self.add_button.clicked.connect(self.add_block)
        layout.addWidget(self.add_button)

        self.show_button = QPushButton("Показать весь блокчейн")
        self.show_button.setFont(QFont('Arial', 11))
        self.show_button.clicked.connect(self.show_blockchain)
        layout.addWidget(self.show_button)

        self.try_delete_button = QPushButton("Попробовать удалить блок")
        self.try_delete_button.setFont(QFont('Arial', 11))
        self.try_delete_button.clicked.connect(self.try_delete_block)
        layout.addWidget(self.try_delete_button)

        self.setLayout(layout)

    def add_block(self):
        new_block = next_block(self.last_block, f"Данные блока #{len(self.blockchain)}")
        self.blockchain.append(new_block)
        self.last_block = new_block

        self.text_output.clear()
        self.text_output.append(
            f"\nБлок #{new_block.index} добавлен."
        )

    def show_blockchain(self):
        self.text_output.clear()
        self.text_output.append("\nТекущий блокчейн")
        self.text_output.append(f"Общее количество блоков: {len(self.blockchain)}\n")
        for block in self.blockchain:
            self.text_output.append(f"Блок #{block.index}\n"
                                    f"Хеш: #{block.hash}\n")

    def try_delete_block(self):
        self.text_output.clear()
        self.text_output.append("\nОШИБКА: структура блокчейна неизменяема.")


# Запуск приложения
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BlockchainApp()
    window.show()
    sys.exit(app.exec_())
