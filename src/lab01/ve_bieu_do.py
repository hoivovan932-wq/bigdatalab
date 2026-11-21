import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('src/lab01/ket_qua_blocksize.csv')
stats = df.groupby('block_mb')['giay'].agg(['mean', 'std'])
ax = stats['mean'].plot(kind='bar', yerr=stats['std'], capsize=4, color='skyblue', edgecolor='black')
plt.title('Thoi gian ghi 1GB theo kich thuoc Block')
plt.xlabel('Block Size (MB)')
plt.ylabel('Thoi gian trung binh (giay)')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('src/lab01/bieu_do_blocksize.png')
print('Da luu bieu do thanh cong!')
