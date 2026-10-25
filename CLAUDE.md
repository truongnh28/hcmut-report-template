# CLAUDE.md

Quy tắc khi dùng các template trong repo này để viết báo cáo, slide hoặc paper. Đọc hết trước khi viết.

## Chọn template

| Loại tài liệu | Template | Build |
|---|---|---|
| Bài tập lớn, assignment môn học | `report-assignment/` | `latexmk -pdf template.tex` |
| Báo cáo thực tập, đề cương luận văn, luận văn | `report-thesis/` | `latexmk main.tex` (ra `out/main.pdf`) |
| Slide báo cáo thầy, slide bảo vệ, slide hội nghị | `slides/` | `latexmk main.tex` (ra `out/main.pdf`) |
| Paper nộp hội nghị | class của hội nghị, không dùng repo này | xem mục Paper |

- Copy cả thư mục template ra chỗ làm việc, không sửa template gốc cho một đề tài cụ thể.
- Điền mọi chỗ `[...]`. Thông tin cá nhân chưa biết (ngày sinh, địa chỉ, ...) thì để `[điền]`, không bịa.
- Không dùng `minted` (máy không có `pygmentize`); code dùng `listings`.
- Lỗi font tiếng Việt: giữ `vntex` + `babel` như template, không đổi encoding.

## Nguyên tắc chung (mọi loại tài liệu)

- **Nguồn sự thật duy nhất.** Mọi con số, mệnh đề, hình lấy từ một nguồn: bài báo đã nộp, bảng kết quả, hoặc repo. Không thêm claim mới, không làm tròn khác nguồn. Bản tiếng Việt và tiếng Anh phải có đúng cùng bộ số.
- **Chỉ nói đúng cái đã đo.** Câu kết luận nói đúng đại lượng đã tính (đo tỉ lệ bỏ sót ở một mức ngân sách thì không viết thành "ngân sách cần thiết"). Kết quả chính luôn đặt cạnh baseline "không làm gì"; nếu baseline chính thua cả "không làm gì" thì headline là một phát biểu về baseline.
- **Đứng độc lập.** Tài liệu chỉ nói về khoa học, không nói về quan hệ với tài liệu khác hay với bản nháp của chính nó: không mã nội bộ (D28, Gate 4, ...), không ngày tháng tuyệt đối của quá trình làm (nói thứ tự sự kiện), không "bản trước / giờ / đã rút lại", không biện minh bằng tài liệu người đọc không có (prereg, spec, bản nháp của thầy), không `\texttt` tên file nguồn.
- **Không giấu sự thật bất lợi.** Dự đoán sai, lựa chọn đưa ra sau khi thấy dữ liệu dev, phần mô phỏng hay replay, phần chưa đo: mỗi điều nói đúng một lần, như một sự thật, ở đúng chỗ (Threats / thiết kế thí nghiệm). Không tự bình luận kiểu "chúng tôi nói thẳng", "chứ không giấu".
- **Không có danh sách "chúng tôi không khẳng định...".** Phạm vi nói theo hướng khẳng định; giới hạn liệt kê một lần trong phần Threats / Hạn chế.
- **Không chỉnh tham số để ra con số mong muốn.** Dựng thí nghiệm trung thực, chỉ tinh chỉnh trên dev trước khi chốt, báo cáo đúng kết quả.
- **Văn phong.** Câu ngắn, khẳng định, mỗi đoạn một ý; mỗi thuật ngữ định nghĩa một lần rồi dùng lại; chủ ngữ cụ thể, động từ thay danh từ hoá; nói cơ chế thay vì tả dữ liệu. Không câu báo trước câu sau ("Lý do mang tính cấu trúc."), không ẩn dụ hay câu đúc kết kiểu châm ngôn, không câu nhồi số (tối đa 2 số mỗi khối).
- **In đậm.** `\textbf` 0 lần trong văn bản chạy. Chỉ dùng cho nhãn trong khung trả lời RQ, tên phần của định nghĩa/định lý. Nghiêng cho thuật ngữ tại chỗ định nghĩa.
- **Thuật ngữ.** Giải thích ngắn ở lần đầu xuất hiện, kể cả thuật ngữ "ai cũng biết" (lockfile, bootstrap, CVaR, ...).
- **Tiếng Việt.** Từ tiếng Việt không rõ nghĩa thì giữ tiếng Anh (vd. "harm" thay "tác hại", "task", "commit"). Một khái niệm một từ, nhất quán từ đầu đến cuối. Dịch là dịch sát bản tiếng Anh theo từng mục, không viết lại. Dấu phẩy thập phân trong bản tiếng Việt.
- **Hình.** Mỗi kết quả chính có một hình; bảng giữ giá trị chính xác, hình kể câu chuyện. Caption 1–2 câu: hình cho thấy gì và đọc thế nào. Công thức viết bằng LaTeX, không chụp ảnh. Hình tiếng Việt và tiếng Anh giống hệt nhau về số.
- **Làm tự nhiên hơn.** Sửa tay, chỉ đổi nhịp câu, không thêm nghĩa (kiểm tập token và tập số không đổi). Không dùng model "humanizer": đã thử, kết quả không dùng được.

## Báo cáo dài (`report-thesis/`: thực tập, đề cương, luận văn)

- **Giữ cấu trúc của template / báo cáo trước.** Tên mục theo mẫu; chương 2 mở bằng Định nghĩa bài toán / Lịch sử phát triển / Các bối cảnh ứng dụng / Thách thức trước mô hình hình thức; các chương giữa kết thúc bằng "Tổng kết chương"; chương cuối có "Định hướng phát triển" và "Kế hoạch và tiến độ thực hiện".
- **Tiêu đề chương** ở vị trí như mẫu gốc, chữ đen, không hộp đen; phụ lục dùng nhãn "Phụ lục".
- **Độ dài** theo yêu cầu đợt (báo cáo thực tập khoảng 70 trang).
- **Bám bài báo.** Báo cáo viết từ bài báo đã nộp: mọi chỗ sửa phải bám bài báo, không thêm claim mới; caveat nào bài báo có thì báo cáo mang theo. Bảng tính từ công thức (không đo) phải ghi rõ là tính.
- **Điều kiện ẩn đặt cạnh bảng chính.** Giả định làm kết quả đẹp hơn (biết trước tham số, tham số chỉnh theo từng điều kiện, mọi episode đều bị tấn công, ...) ghi ngay trước/sau bảng kết quả chính, không chôn trong phụ lục.
- **Tóm tắt / kết luận.** Báo cáo có thể mở bằng điểm yếu nếu tác giả chọn vậy; paper hội nghị thì không (xem dưới).
- **Lời cam đoan** có một câu về việc dùng trợ lý AI (hỗ trợ viết mã, trau chuốt câu chữ; câu hỏi, thiết kế, phân tích là của tác giả).
- **Ẩn danh.** Khi bài báo gốc đang review double-blind, không đăng báo cáo công khai.

## Slide (`slides/`)

- **Báo cáo nhanh cho thầy (~15 phút):** khoảng 10–14 slide, thật cơ bản, dễ hiểu, đi thẳng vào trọng tâm. Thứ tự: Bài toán (phải có slide đặt vấn đề, có ví dụ cụ thể) → Ý tưởng → Cách làm → Câu hỏi nghiên cứu → Kết quả (mỗi RQ một slide, mở bằng câu trả lời và một con số quyết định) → Tóm tắt → Tiến trình / việc còn lại.
- **Kết quả theo paper.** Số, hình, bảng trên slide lấy y nguyên từ paper; ghi nhãn bằng chứng (đo / mô phỏng). Không đưa số dự phóng hay số nháp.
- **Một slide một ý**, chữ ít, hình nhiều; công thức nào khó thì vẽ hình minh hoạ cho công thức.
- **Không nhắc đề tài khác.** Slide của đề tài nào chỉ nói về đề tài đó, kể cả khi dùng lại template hay hình từ đề tài khác.
- **Kịch bản nói.** Viết lời nói cho từng slide trong file `<tên-slide>-script.md` cạnh file `.tex`: mỗi slide một đoạn, ghi thời lượng trong ngoặc, xưng "em" với thầy, số nói đúng như trên slide.
- **Slide dự phòng** đặt sau `\appendix`; footer chỉ đếm tới `\label{endmain}`.
- Bỏ slide không mang giá trị cho người nghe (hướng dẫn sử dụng, chi tiết kỹ thuật vụn) khi được yêu cầu rút gọn.

## Paper hội nghị (không dùng template ở đây)

- **Class của hội nghị, đúng từng option.** Đọc CFP trước khi viết (vd. ACM `acmsmall,screen,review,anonymous`), dựng đúng class từ bản nháp đầu, kiểm giới hạn trang theo đúng chữ của CFP.
- **Abstract** ≤ 8 câu, ≤ 210 từ, 4 phần: bối cảnh và vấn đề / phương pháp / kết quả với 2–3 con số quyết định / ý nghĩa. Abstract và kết luận chỉ nêu điểm mạnh; caveat để trong thân bài.
- **Introduction**: các thành phần của bài toán, mỗi cái một mệnh đề kèm ví dụ cụ thể → đi qua hình tổng quan bằng số của bài → bối cảnh và các công trình trước (gom nhóm) → khoảng trống dưới dạng câu hỏi mở → "We answer this question by ..." → các RQ → 3–4 đóng góp, mỗi cái một câu → roadmap đủ mọi mục.
- **Bắt buộc**: bảng map RQ → mô hình/mệnh đề dự đoán → phân tích kiểm tra → hình/bảng; bảng so sánh mô hình với các mô hình trước (kiểm từng ô với nguồn gốc); bảng "vì sao chọn mô hình này" (lựa chọn, lý do có trích dẫn, kiểm ở đâu).
- **Phương pháp > kết quả** (≈ 7 trang so với ≈ 5 trang một cột). Mỗi RQ trong Results: khung Answer (câu trả lời, 1 số, 1 caveat giới hạn phạm vi) / Evidence / Why / Predictions (báo cả dự đoán sai) / Robustness. Không có nguồn cho Why thì để `% TODO(author)`, không bịa.
- **Toán.** Kết quả suy từ bất đẳng thức chuẩn gọi là Proposition, trích công cụ ở đầu mục; định nghĩa tách phần có nhãn, phương trình hiển thị, có ví dụ sau mỗi định nghĩa; gọi đúng tên solution concept.
- **Threats** ba đoạn Construct / Internal / External, mỗi giới hạn một mệnh đề.
- Trước khi nói "sạch" hay "sẵn sàng nộp": chạy `audit_referents.py` và `check_paper.py` của skill `writing-papers-advisor-style`, rồi **đọc từng câu** được in ra. Grep chỉ là mức sàn, chưa bao giờ đủ.

## Tin nhắn / email gửi thầy

- Câu văn nghiêm túc, ngắn; trạng thái lên đầu để thầy nhìn là biết đang làm gì, tới đâu; chi tiết để trong repo, gửi link.

## Review do Claude làm

- Đánh giá độc lập, nghiêm khắc, không nịnh. Kiểm lại số bằng nguồn trước khi kết luận.

## Git

- Không thêm dòng `Co-Authored-By` vào commit.
- Stage file theo đường dẫn, không `git add -A` trong repo đề tài; người dùng tự merge.
- Repo này public: không commit nội dung, hình, số liệu, tên đề tài hay thông tin cá nhân của báo cáo thật. Chỉ commit khung template.
