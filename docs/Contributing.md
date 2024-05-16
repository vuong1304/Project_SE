## Hướng dẫn :information_source:

Chúng tôi biết rằng bạn muốn giúp đỡ chúng tôi trong việc phiên dịch một cách nhanh chóng nhưng chúng tôi có một quy trình để đảm bảo rằng việc dịch thuật diễn ra trôi chảy.

### Nhận tài liệu cần dịch

1. Bắt đầu dịch  :white_check_mark:

Trong những phần tiếp theo, chúng tôi sẽ hướng dẫn bạn cách clone bản dịch về máy và nộp bản dịch bằng cách thực hiện Pull Request.

### Clone kho lưu trữ và bắt đầu dịch

Thật tuyệt vời nếu đây là lần đầu tiên bạn đóng góp cho cộng đồng phần mềm mã nguồn mở! Trong phần này, Chúng tôi sẽ hướng dẫn bạn thực hiện một quy trình sử dụng Git và Github để lưu toàn bộ kho lưu trữ về máy tính cá nhân của bạn để bạn sẵn sàng cho bản dịch đầu tiên.

#### Những công cụ cần thiết

Bạn cần cài đặt những công cụ sau trong máy tính của bạn để có thể đóng góp:

* [Git](https://git-scm.com/)
* Một terminal - cửa sổ gõ dòng lệnh (ví dụ: PowerShell, Windows Terminal, Git Bash...)
* Một chương trình chỉnh sửa văn bản (ví dụ: Notepad++, Sublime, Visual Studio Code...). Chúng tôi khuyến cáo Visual Stdio Code vì hỗ trở tốt định dạng Markdown và có các tiện ích bổ sung hữu ích.

#### Quy trình

1. Đầu tiên, bạn cần Fork kho lưu trữ về kho của bạn.

    Điều hướng hướng đến kho lưu trữ gốc. Hãy bấm vào nút **Fork** ở góc phía trên, bên phải của kho lưu trữ và chờ Github sao chép kho lưu trữ gốc về tài khoản cá nhân của bạn.

    Bản sẽ được chuyển hướng đến một kho lưu trữ tương tự như kho lưu trữ gốc với tên người sở hữu là bạn.

1. Tiếp theo, bạn cần Clone kho lưu trữ về máy để tiện làm việc.

    Tại kho lưu trữ mới bạn sở hữu, bấm vào nút **Clone or Download** màu xanh lá bên tay phải và sao chép đường trong pop-up xuất hiện.

    Điều hướng đến nơi bạn muốn chứa kho lưu trữ trên máy tính cá nhân của bạn, mở terminal tại đây (bạn có thể click chuột phải và chọn `Git Bash Here`) và thực hiện câu lệnh sau với `<URL>` là đường link bạn sao chép phía trên.

    ```bash
    git clone <URL>
    ```
    
    Chờ Git clone toàn bộ kho lưu trữ về máy bạn. Sau đó, hãy điều hướng termiank vào trong thư mục chứa kho lưu trữ:

    ```bash
    cd docs
    ```

1. Tạo 1 branch (nhánh phát triển) mới cho kho lưu trữ.

    Khi bạn clone kho lưu trữ về, bạn sẽ được mặc định trong nhánh `master`, nơi chỉ chứa những tài liệu dịch chính thức. Những thay đổi của bạn trong kho lưu trữ này nên nằm trong một nhánh "tại chỗ" mới.

    Khi bạn đã trong thư mục chứa kho lưu trữ, thực hiện dòng lệnh sau để tạo 1 nhánh mới với `<TÊN-NHÁNH>` đại diện tài liệu bạn chuẩn bị dịch. Ví dụ: `tutorial-7`, `docs-index`, `code-of-conduct`...

    ```bash
    git checkout -b <TÊN-NHÁNH>
    ```

    Nếu bạn dùng terminal Git Bash (hoặc khi bạn chạy lệnh `git branch`), bạn sẽ thấy tên nhánh của bạn đã được đổi từ `master` sang tên mới.

1. Mở file Markdown của tài liệu bạn đã được chỉ định bằng công cụ gõ văn bản yêu thích và bắt đầu chỉnh sửa nội dung sang Tiếng Việt.

### Nộp bản dịch (Commit & Push)

#### Commit

Sau khi chỉnh sửa nội dung của tài liệu, bạn sẽ cần phải commit những thay đôi này bằng cách thực hiện những lệnh sau:

```bash
git add <TÊN-FILE>
git commit -m <TIN-NHẮN>
```

với

* `<TÊN-FILE>` là đường dẫn đến (những) file bạn chỉnh sửa. Cách nhanh nhất để lấy đường dẫn đến file là dùng lệnh `git status`. Lệnh này sẽ hiển thị những file đã bị thay đổi hoặc thêm mới trong phần `Modified` hoặc `Untracked`.
* `<TIN-NHẮN>` là mô tả cho mục đích của chỉnh sửa bạn đã thực hiện

**Lưu ý:**

Việc commit không nên được thực hiện khi bạn trên nhánh master. Xem tên nhánh hiện tại của bạn bằng lệnh `git branch`. Nếu bạn còn trên nhánh master, có thể bạn đã chưa chạy lệnh `git checkout` ở phần trên.

Trước khi commit,  bạn luôn cần phải chỉ ra những file cần được bao gồm trong commit. Việc này được thực hiện bằng lệnh `git add`.

Việc **commit** có thể được thực hiện nhiều lần trong 1 bản dịch. Mỗi khi file bị thay đổi, bạn phải dùng lệnh `git add` trước khi commit mới.

Mỗi **commit** chỉ nên phục vụ 1 mục đích duy nhất được miêu tả trong phần tin nhắn (message). Phần tin nhắn nên được ghi bằng Tiếng Anh để những thành viên bảo trì quốc tế có thể theo dõi dự án.

**Ví dụ về cách commit:**

```bash
git add CONTRIBBUTING.md
git commit -m "Add CONTRIBUTING.md with basic structure"
```

```bash
git add CONTRIBBUTING.md
git commit -m "Update fork/clone instruction for CONTRIBUTING.md"
```

```bash
git add CONTRIBBUTING.md
git commit -m "Complete CONTRIBUTING.md translation"
```

#### Push

Sau khi đã hoàn thành bản dịch của một tại liệu, việc bạn cần làm là **push** (đẩy) những thay đổi bạn thực hiện lên kho lưu trữ Github của bạn sở hữu. Việc này được thực hiện bằng lệnh sau với `<TÊN-NHÁNH>` là tên nhánh bạn đặt ban đầu.

```bash
git push origin <TÊN-NHÁNH>
```

Cách nhanh nhất để xem tên nhánh hiện tại của bạn là dùng lệnh `git branch`, tên nhánh hiện tại của bạn sẽ được đánh dấu bằng ký tự `*`. Nếu bạn dùng terminal Git Bash, tên nhánh của bạn sẽ được hiển thị ở cuối tên bạn.

**Lưu ý:**

Bạn không nên chạy lệnh `git push origin master` để push chỉnh sửa của bạn lên nhánh `master`. Bạn chỉ nên push lên nhánh riêng của bạn.

Phần tiếp theo, chúng tôi sẽ hướng dẫn cách tạo một Pull Request trên Github để nộp bản dịch tài liệu của bạn. Khi đó, các thành viên bảo trì sẽ xem qua bản dịch của bạn để gộp vào nhánh `master` của kho lưu trữ gốc.

#### Tạo Pull Request

Phần cuối cùng bạn cần làm trong quy trình này là tạo 1 Pull Request (PR) để nộp bản dịch của bạn cho kho lưu trữ chính thức từ kho do bạn sở hữu. Việc này rất đơn giản và được thực hiện thông qua website của Github.

1. Điều hướng đến kho lưu trữ gốc.

1. Nếu bạn đã push những commit từ máy bạn lên kho lưu trữ do bạn sở hữu, Github sẽ hiển thị 1 dòng thông báo trên nền màu vàng nhạt ngay phía dưới phần mô tả của kho lưu trữ. Nhấm vào nút **Compare and Pull Reuqest** màu xanh lá tại cuối dòng thông báo. Bạn sẽ được điều hướng đến trang tạo PR.

1. Nhập vào tiêu đề của PR và mô tả của những thay đổi quan trọng bạn đã thực hiện (nếu cần thiết).

    Tiêu đề của PR được đặt theo cú pháp sau **bằng Tiếng Anh**:

    ```text
    [Translation] <LOẠI-TÀI-LIỆU>/<TÊN-TÀI-LIỆU>
    ```

    với

    * `<LOẠI-TÀI-LIỆU>` có thể là `community`, `tutorial` hoặc `docs`.
    * `<TÊN-TÀI-LIỆU>` là tên file Markdown của tài liệu bạn đã dịch (loại trừ phần mở rộng `.md`).

    **Một số tiêu đề PR mẫu:**

    * `[Translation] tutorial/index`
    * `[Translation] tutorial/part-zero`
    * `[Translation] docs/gatsby-cli`

    Mô tả của PR có thể là câu hỏi cho những điểm bạn không chắc chắn trong tài liệu bạn dịch hoặc cần ý kiến từ cộng đồng.

    Những thành viên đóng góp và bảo trì khác được khuyến khích tích cực xem qua PR của những thành viên khác để đảm bảo chất lượng cho những bản dịch.

1. Sau khi đã nhập vào tiêu đề và mô tả cho PR. Hãy đảm bảo rằng...

    * Mục `base` hiển thị giá trị `master`
    * Mục `compare` hiển thị giá trị `<TÊN-GITHUB>/<TÊN-NHÁNH>`

    Điều này có nghĩa rằng bạn đang tạo một Pull Request để yêu cầu gộp thay đổi trong nhánh mới của bạn ở kho lưu trữ do bạn sở hữu vào nhánh `master` của kho lưu trữ gốc.

1. Khi đã kiểm tra đầy đủ các trường dữ liệu trên, bấm nút **Create a Pull Request**.

1. Cuối cùng, yêu cầu gộp thay đổi bạn thực hiện đã được tạo. Vui lòng đợi nhóm bảo trì của Gatsby duyệt qua và gộp vào kho lưu trữ chính thức.

## Ghi chú và khuyến cáo :thumbsup:

1. Luôn kiểm tra lỗi chính tả và ngữ pháp kỹ lưỡng, dịch tài liệu với cách dùng từ và hành văn văn tốt nhất có thể.

1. Tránh thêm hoặc xóa bớt hàng trong tài liệu gốc. Từng hàng chữ trong tài liệu gốc nên được dịch thành từng hàng tương ứng trong Tiếng Việt. Điều này có thể được kiểm tra sau khi dịch bằng cách so sánh 10 hàng đầu tiên và 10 hàng cuối cùng giữa tài liệu gốc và tài liệu dịch. Chúng nên là từng cặp hàng tương ứng với nhau.

1. Luôn giữ ngôn ngữ trung lập, tránh phụ thuộc vào giới tính, tuổi tác, vùng miền, sắc tộc, văn hóa, tôn giáo, tư tưởng chính trị...

1. Khi người đóng góp không thể dịch 1 từ nào đó, bạn hoàn toàn có thể dùng [Google Dịch](https://translate.google.com.vn/#view=home&op=translate&sl=en&tl=vi). Vui lòng đừng dịch cả trang bằng Google Dịch vì sẽ bị mất đi ý nghĩa của trang.

1. Bên cạnh việc dịch thuật, các bạn cũng có thể đọc qua các tài liệu đã được dịch và đóng góp bằng cách phát hiện ra những lỗi như lỗi đánh máy, cách dùng từ, dịch sai hoặc cả kể khi bạn có cách dịch tốt hơn cách hiện tại. Chỉ cần tạo một Pull Reuqest để sửa lỗi và chúng tôi sẽ trân trọng đóng góp của bạn.

### Những công cụ/tiện ích hỗ trợ dịch :wrench:

Nếu bạn dùng Visual Studio Code (VSCode) phục vụ việc chỉnh sửa bản dịch, bạn có thể cài đặt các tiện ích mở rộng sau để tiện cho việc chỉnh sửa file định dạng Markdown:

* [Github Markdown Preview](https://marketplace.visualstudio.com/items?itemName=bierner.github-markdown-preview): Sau khi cài đặt, dùng tổ hợp phím `Ctrl + Shift + V` để kích hoạt chế độ xem trước của Github cho file định dạng Markdown. Tiện ích cho phép VSCode hiển thị xem trước cho file Markdown hiện tại như Github sẽ hiển thị trước khi bạn push lên kho lưu trữ cá nhân.

* [markdownlint](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint): Cộng cụ giúp bạn gõ tài liệu Markdown tốt hơn và theo khuôn mẫu hơn.
