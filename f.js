let captchaValido = false;
let tokenCaptcha = null;

function captchaSucesso() {
  captchaValido = true;
  tokenCaptcha = crypto.randomUUID(); // token único
  document.getElementById("btnContinuar").style.display = "inline-block";
  document.getElementById("btnContinuar").dataset.token = tokenCaptcha;
}

document.getElementById("btnContinuar").addEventListener("click", function () {
  const tokenBotao = this.dataset.token;

  if (!captchaValido || !tokenBotao || tokenBotao !== tokenCaptcha) {
    alert("🚫 Acesso bloqueado. Validação inválida.");
    location.reload();
    return;
  }

  entrarSeguro(tokenBotao);
});

function entrarSeguro(token) {
  if (token !== tokenCaptcha) {
    alert("🚫 Tentativa de burla detectada.");
    location.reload();
    return;
  }

  window.location.href = "https://j-s-yt.github.io/link/";
}
