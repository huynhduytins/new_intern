
##  Xây dựng giao diện phần mềm quản lý nhân viên bằng Tkinter

Để chạy được ta chỉ cần clone tất cả các file về chung một thư mục và chạy file ```main.py```


Packet cần cài đặt:

- PIL (Python Imaging Library -> Dùng để chèn ảnh):  

        pip install Pillow
## Demo
Chương trình dành cho người quản lý có thể chỉnh sửa và thêm bớt nhân viên. Chương trình có thể tự động tính công cho nhân viên sau khi cập nhật một số thành phần:
```Lương căn bản``` + ```(0.05 * lương căn bản)``` **nếu như số con > 2** + ```(0.1 * lương căn bản)``` **nếu như trình độ văn hóa là cao học** + ```(0.04 * lương căn bản * số ngày làm thêm)``` - ```(0.05 * lương căn bản * số ngày nghỉ không phép)```


**Chạy chương trình**


Ta phải nhập đúng **tên đăng nhập** ```admin123``` và **mật khẩu** ```123456789```


![Capture](https://user-images.githubusercontent.com/82378378/165754109-9774a656-b7be-42e0-87f5-e1a13ec1ac57.PNG)


![Capture1](https://user-images.githubusercontent.com/82378378/165754107-f3391b18-82d5-4179-b407-6a4f008a0c38.PNG)


**Màn hình đăng nhập**


![Capture2](https://user-images.githubusercontent.com/82378378/165754103-fcd76ff2-544a-4ca6-8b0a-742eea6eac26.PNG)


**Chọn ```SHOW THE LIST```Hiển thị danh sách nhân viên có sẵn đọc từ file ```DsNhanVien.csv```**


![Capture3](https://user-images.githubusercontent.com/82378378/165754099-31d3332b-f3b7-4d35-a4da-9887f32adf2b.PNG)


**Chọn ```ADD A EMPLOYEE``` để thêm vào 1 nhân viên mới với ```ID``` được cấp sẵn**

![Capture6](https://user-images.githubusercontent.com/82378378/165754087-98be418b-9830-46e5-b2c0-9251a6b203b2.PNG)


**Có một số ràng buộc khi nhập thông tin nhân viên. Khi nhập không đúng, chương trình sẽ báo lỗi**


![Capture4](https://user-images.githubusercontent.com/82378378/165754097-25deb1cd-7b6e-4a22-abd3-12fc8f5872b5.PNG)



![Capture5](https://user-images.githubusercontent.com/82378378/165754093-94775c2b-7680-43a7-9340-cf8eeee4e483.PNG)



**Hiển thị lại danh sách nhân viên sau khi thêm 1 nhân viên mơi**


![Capture7](https://user-images.githubusercontent.com/82378378/165754082-67cab666-4720-4062-9af0-a977ff5efe09.PNG)



**Khi chọn ```DELETE EMPLOYEE``` hoặc ```MODIFY EMPLOYEE``` ta phải nhập đúng ID của nhân viên**


![Capture8](https://user-images.githubusercontent.com/82378378/165754081-d7b3c430-dafa-4341-beec-1d18e012540f.PNG)

**Chọn ```DELETE EMPLOYEE```**


![Capture9](https://user-images.githubusercontent.com/82378378/165754073-09e85089-4643-472e-9959-0db8a5c5ea66.PNG)

**Chương trình sẽ hỏi lại có chắc muốn xóa hay không**


![Capture10](https://user-images.githubusercontent.com/82378378/165754071-9266d7a5-30b5-4962-a6df-956a126a7a2a.PNG)


**Hiển thị lại chương trình sau khi xóa nhân viên**


![Capture11](https://user-images.githubusercontent.com/82378378/165754066-740f40ee-1fcd-432a-922c-6d1183477c16.PNG)


**Chọn ```MODIFY EMPLOYEE```**


![Capture12](https://user-images.githubusercontent.com/82378378/165754060-1579512e-972b-485f-ae93-4a8c72e32e7b.PNG)


**Khi nhấn ```SAVE``` Chương trình sẽ tự động tính lại số lương thực tế sau khi cập nhật 1 số thành phần ảnh hưởng đến mức lương**

![Capture14](https://user-images.githubusercontent.com/82378378/165754058-91d53f1a-1ad3-444a-ae7e-d8b2251aab7c.PNG)

**Hiển thị lại danh sách nhân viên sau khi chỉnh sửa**

![Capture15](https://user-images.githubusercontent.com/82378378/165754056-7fdc3483-64f2-4f80-8490-831916d8ff30.PNG)

**Chọn ```CHANGE THE PASSWORD``` để cập nhật lại mật khẩu. Mật khẩu mới phải đảm bảo trên 8 ký tự**


![Capture16](https://user-images.githubusercontent.com/82378378/165754041-418dd735-58a8-4269-9ac9-d238ec521e3f.PNG)
