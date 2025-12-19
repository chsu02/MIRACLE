# MIRACLE 奇蹟事務所 — 台股工具與選股範例 🚀

**Repository:** https://github.com/chsu02/MIRACLE.git

**股神巴菲特的老師：價值投資之父葛拉漢的選股秘訣（淨營運資本法）**

影片參考：https://www.youtube.com/watch?v=OlnprlpHjQo&list=PLzr9EpvIZ0Grpd_W6d1A7CQvLh_yDveX0&index=1

---

## 簡介
本專案收錄數支小型 Python 腳本，主要用途為台股資料擷取、簡單選股篩選、以及繪製即時 K 線圖。主要腳本為教材 / 工具性質，適合用於學習、研究或快速原型。

## 特色 ✨
- 使用爬蟲與公開 API（如 Yahoo、TWSE、yfinance、twstock）取得財務與即時報價資料
- 範例包含：淨營運資本選股法、即時報價查詢、K 線繪圖、上市股代碼匯出為 Excel
- 以學習與參考為主，非交易建議（請務必自行驗證與風險控管）

## 快速開始 ✅
1. 建議建立虛擬環境（例如 venv 或 conda）：
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```
2. 安裝相依套件：
   ```bash
   pip install -r requirements.txt
   ```
3. 常用指令：
   - `python 淨營運資本.py`：以淨營運資本法篩選股票（條件：股價 < (流動資產 - 總負債) / 股數）
   - `python 即時資料.py`：透過 `twstock` 取得即時報價（預設示範代號 `1215`）
   - `python 及時k線.py`：以 `yfinance` 取得時序資料並用 Plotly 顯示 K 線圖（示範 ticker：`AAPL`，可改為 TWSE 代號如 `2330.TW`）
   - `python 股票追蹤.py`：爬取 TWSE 上市股票代號/名稱並寫入 `上市股追蹤.xlsx`

## 注意事項 ⚠️
- 部分腳本採用網頁爬蟲（Yahoo、TWSE），網站格式變動或連線問題會造成程式錯誤，建議加入錯誤處理與重試機制。
- 請遵守目標網站使用條款與限制流量頻率（rate limiting）。
- 這些工具僅供學習/研究用途，不構成投資建議。

## 檔案概覽 🔍
- `淨營運資本.py` — 爬取財報與股價並以淨營運資本法篩選股票
- `即時資料.py` — `twstock` 即時報價示範
- `及時k線.py` — `yfinance + Plotly` 的 K 線與成交量圖示範
- `股票追蹤.py` — 匯出上市股名稱與代號至 `上市股追蹤.xlsx`
- `上市股追蹤.xlsx` — 腳本輸出檔案（由 `股票追蹤.py` 產生）

## 貢獻指南 💡
歡迎提出 Issue 或 Pull Request：
- 建議改進：加入 CLI 參數、改善錯誤處理、增加測試
- 若需要，我可以協助新增 `LICENSE`（例如 MIT）與簡短的 `CONTRIBUTING.md`

## 授權 / License
目前尚未指定授權。如果你希望，我可以為專案新增 MIT 授權檔案（`LICENSE`）。

---

若要，我可以：
1. 幫你把 `README.md` 更新成這個內容（已替換）
2. 接著建立 `LICENSE`（MIT）並提交成一個 commit

需要我幫你把變更提交到 git（commit / branch / PR）嗎？