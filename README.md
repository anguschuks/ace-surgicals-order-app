# ACE Surgicals Order App

A lightweight catalogue app for ACE Surgicals Ltd (RC 7117725, Kano) with search, category filters, a cart and WhatsApp checkout.

Customers browse 500+ medical, surgical and laboratory items with prices per unit, build an order and send it straight to the sales team on WhatsApp at **+234 907 760 0522**.

## What's in this repository

| File / folder | What it is |
|---|---|
| `index.html` | The app. One self-contained file: open it in a browser or host it on any website. |
| `ACE_Surgicals_Products.xlsx` | Editable product list (No, Category, Product, Description, Price, Photo, Show). |
| `photos/` | Put product pictures here and type the file name in the sheet's Photo column. |
| `source/` | Files used to rebuild `index.html` (template, product data, logo, build script). |

## Features

- Search by name, description or catalogue number; filter by category; sort by name or price
- Cart with quantities, totals and customer details (name, phone, facility, delivery address, note)
- **Send order on WhatsApp**: opens a chat with +234 907 760 0522 with the order already typed
- **Send as a picture**: creates an order image to share through WhatsApp
- **Chat with us** button for general enquiries
- **Order code and "View official order" link** on every order, so staff can see the true order at official prices even if the WhatsApp text was edited
- **Staff: check an order** (footer link, or add `#verify` to the address): paste a WhatsApp order to check it against the price list

## Updating prices, names and items

### Option A: live Google Sheet (recommended)

1. Upload `ACE_Surgicals_Products.xlsx` to Google Drive and open it with Google Sheets.
2. **File → Share → Publish to web**, choose the **Products** sheet and **Comma-separated values (.csv)**, then copy the link.
3. In `index.html`, paste the link between the quotes in `const SHEET_CSV_URL="";` near the top of the script.

After that, edits in the sheet show in the app within a few minutes:
- **Change a price or name:** edit the cell.
- **Add an item:** add a row with a new number.
- **Hide an item:** set Show to `No`.

If the sheet can't be reached, the app uses its built-in list.

### Option B: rebuild the built-in list

Edit `source/products.json`, then run `python3 source/build.py` to regenerate `index.html`.

## Photos

Put each item's picture in the Photo column of the sheet, either as:
- a full web link (`https://...`), or
- a file name in the `photos/` folder (`hospital-bed.jpg`).

Square or 4:3 pictures on a white background look best. Items without a photo show an illustration.

## Settings

Near the top of the script in `index.html`:

| Setting | Purpose |
|---|---|
| `SHEET_CSV_URL` | Google Sheets CSV link for the live product list |
| `PHOTO_FOLDER` | Folder for photo file names (default `photos/`) |
| `WA_NUMBER` | WhatsApp number orders go to (`2349077600522`) |
| `APP_URL` | Address used in "View official order" links; leave empty to use the address the app is opened from |

## Hosting

**GitHub Pages:** in this repository go to **Settings → Pages**, set **Source** to *Deploy from a branch*, choose `main` and `/ (root)`, then click **Save**. The app will be live at `https://anguschuks.github.io/ace-surgicals-order-app/`.

It can also be uploaded to `acesurgicalsltd.com` as-is, for example as `/order/index.html` with the `photos` folder beside it.

---

ACE Surgicals Ltd · 15/16 Post Office Rd, Fagge, Kano, Nigeria · +234 907 760 0522 · acesurgicalsltd@gmail.com
