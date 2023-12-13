// textarea: code-to-format
// textarea: output-formatted-code

{
  /* <script src="https://unpkg.com/prettier@2.3.2/standalone.js"></script>
<script src="https://unpkg.com/prettier@2.3.2/parser-babel.js"></script> */
}

function formatCode(inputCode) {
  return prettier.format(inputCode, {
    parser: "babel",
    plugins: prettierPlugins,
  });
}

// document
//   .getElementById("submit-code-to-format")
//   .addEventListener("click", function () {
//     const inputCode = document.getElementById("code-to-format").value;
//     const formattedCode = formatCode(inputCode);
//     document.getElementById("output-formatted-code").value = formattedCode;
//   });
