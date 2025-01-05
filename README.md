## 🧮 A variety of bit systems calculator
> [!NOTE]
> This project was created for the discipline "Discrete Mathematic".

The primary objective was to develop practical skills in project structuring, even if the project was relatively straightforward. Through enhancements, I transformed a console application that parsed values from a distinct syntax into a web application.

The structure is divided into two distinct sections: _the server side and the client side_. The client, through an interface developed using **React** and **Bootstrap**, sends JSON requests to a server written in Python using the **Flask** network library, which then responds.

![output_image](https://github.com/user-attachments/assets/975a05b9-4cc9-4198-8ab6-ca1ebb8a9962)

---

### Deployment
```
git clone https://github.com/andrijzyn/Calconv.git
cd calconv

**starting client side**
npm run dev

**in another console | starting server**
cd app
source .venv/bin/activate
python main.py
```

The server has been started in the http://localhost:5173
