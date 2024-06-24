# 會計師資料爬取腳本

這個Python腳本是為了協助學校老師蒐集大量會計師的資料而開發的，用於會計師證照專班的建立。資料集包含台北市會計師公會的兩千多位會員信息，每位會計師的信息包括事務所電話、地址、傳真等。

## 特點

- **自動化資料收集**：使用網頁爬蟲技術從會計師公會網站自動抓取資料。
- **資料解析**：利用BeautifulSoup解析HTML並提取相關信息。
- **資料存儲**：使用Pandas將收集到的資料結構化地存入Excel文件中。

## 需求

- Python 3.x
- BeautifulSoup4
- Pandas
- Requests

## 安裝

1. clone此倉庫：
   ```bash
   git clone https://github.com/yourusername/accountant-data-scraper.git
   ```
2.	進入項目目錄：
   ```bash
   cd accountant-data-scraper
   ```
## 使用方法
1.	運行腳本：
   ```bash
   python3 scraper.py
   ```
2.	腳本將自動爬取資料並保存到名為accountants_data.xlsx的Excel文件中。

方法

	1.	網頁爬蟲：
	•	腳本使用Requests庫發送HTTP請求到會計師公會網站。
	•	使用BeautifulSoup解析HTML內容並提取所需的數據字段。
	2.	資料提取：
	•	使用Chrome的Inspector工具，找出網頁中所需數據在HTML結構中的位置。
	•	使用BeautifulSoup導航HTML並提取相關信息。
	3.	資料存儲：
	•	使用Pandas將資料整理成DataFrame。
	•	將DataFrame寫入Excel文件中，方便訪問和分析。

##挑戰

在開發過程中遇到了多種挑戰，包括處理不同的HTML結構以及確保數據提取的準確性。儘管面臨這些困難，腳本最終成功開發並執行，提供了準確而全面的結果。

##學習成果

通過這個項目，增強了我在網頁爬蟲、資料解析和Python編程方面的技能。此外，強調了數據準確性和驗證的重要性，以確保可靠的結果。

##貢獻

歡迎Fork此倉庫並提交Pull Request。對於重大更改，請先開啟Issue討論您想做的更改。


##聯繫

如有任何問題或建議，請聯繫steve04282009@gmail.com。
