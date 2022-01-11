# -*- coding: utf-8 -*-
import json

command_data = {"[놀자에요]": "놀자에요_half.png",
                "[요에자놀]": "놀자에요_half_transpose.png",
                "[놀자에요반전]": "놀자에요_half_transpose.png",
                "[놀자에몽]": "놀자에몽_half.png",
                "[머쓱해요]": "머쓱해요_half.png",
                "[웃프네요]": "웃프네요_half.png",
                "[추천이요]": "추천이요_half.png",
                "[정말이요]": "정말이요_half.png",
                "[뭐라구요]": "뭐라구요_half.png",
                "[머쓱환에요]": "머쓱환에요_half.png",
                "[웃기구요]": "웃기구요_half.png",
                "[엄지로아콘]": "01_모코코콘1_01_따봉_modified.png",
                "[엄지척]": "01_모코코콘1_01_따봉_modified.png",
                "[야호로아콘]": "01_모코코콘1_03_모야호_modified.png",
                "[모아호]": "01_모코코콘1_03_모야호_modified.png",
                "[크크로아콘]": "01_모코코콘1_06_ㅋㅋㅋㅋ_modified.png",
                "[크크크]": "01_모코코콘1_06_ㅋㅋㅋㅋ_modified.png",
                "[ㅋㅋㅋ]": "01_모코코콘1_06_ㅋㅋㅋㅋ_modified.png",
                "[방긋로아콘]": "01_모코코콘1_09_방긋_modified.png",
                "[방긋]": "01_모코코콘1_09_방긋_modified.png",
                "[방긋방긋]": "01_모코코콘1_09_방긋_modified.png",
                "[해줘로아콘]": "01_모코코콘1_13_줘_modified.png",
                "[해줘]": "01_모코코콘1_13_줘_modified.png",
                "[줘]": "01_모코코콘1_13_줘_modified.png",
                "[안줘로아콘]": "01_모코코콘1_14_안_줘_modified.png",
                "[안줘]": "01_모코코콘1_14_안_줘_modified.png",
                "[빠직로아콘]": "01_모코코콘1_17_빠직_modified.png",
                "[빠직]": "01_모코코콘1_17_빠직_modified.png",
                "[슬퍼로아콘]": "01_모코코콘1_18_슬퍼_modified.png",
                "[슬퍼]": "01_모코코콘1_18_슬퍼_modified.png",
                "[향기로아콘]": "01_모코코콘1_18_슬퍼_modified.png",
                "[향기]": "01_모코코콘1_18_슬퍼_modified.png",
                "[기분좋은향기]": "01_모코코콘1_18_슬퍼_modified.png",
                "[털썩로아콘]": "01_모코코콘1_24_모무룩_modified.png",
                "[털썩]": "01_모코코콘1_24_모무룩_modified.png"}

with open("command.json", "w", encoding="utf-8") as json_file:
    json_file.write(json.dumps(command_data, ensure_ascii=False))
