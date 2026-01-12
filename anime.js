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
}

const observer = new MutationObserver(() => {
  const captcha = document.querySelector(".cf-turnstile");

  if (!captcha && !captchaValido) {
    alert("🚫 Manipulação detectada.");
    location.reload();
  }
});

observer.observe(document.body, {
  childList: true,
  subtree: true,
});

(function (s) {
  (s.dataset.zone = "10455054"),
    (s.src = "https://gizokraijaw.net/vignette.min.js");
})(
  [document.documentElement, document.body]
    .filter(Boolean)
    .pop()
    .appendChild(document.createElement("script"))
);
