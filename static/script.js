const dropZone = document.getElementById("drop-zone");
const fileInput = document.getElementById("file-input");
const fileName = document.getElementById("file-name");
const errorMsg = document.getElementById("error-msg");
const loading = document.getElementById("loading-overlay");
const form = document.getElementById("upload-form");

if (dropZone && fileInput && form) {

    dropZone.addEventListener("click", () => fileInput.click());

    dropZone.addEventListener("dragover", e => {
        e.preventDefault();
        dropZone.classList.add("dragover");
    });

    dropZone.addEventListener("dragleave", () => {
        dropZone.classList.remove("dragover");
    });

    dropZone.addEventListener("drop", e => {
        e.preventDefault();
        dropZone.classList.remove("dragover");

        attachFile(e.dataTransfer.files[0]);
    });

    fileInput.addEventListener("change", () => {
        attachFile(fileInput.files[0]);
    });

    function attachFile(file) {
        if (!file || !file.name.endsWith(".md")) {
            errorMsg.textContent = "❌ Only .md files allowed";
            fileName.textContent = "";
            return;
        }

        const dt = new DataTransfer();
        dt.items.add(file);
        fileInput.files = dt.files;

        fileName.textContent = "📄 Selected file: " + file.name;
        errorMsg.textContent = "";
    }

    form.addEventListener("submit", () => {
        loading.style.display = "flex";
    });
}
