(function () {
  var form = document.getElementById("application");
  var success = document.getElementById("application-success");
  var resetButton = document.getElementById("application-reset");
  var errorEl = document.getElementById("application-error");
  var countEl = document.getElementById("step-count");
  var titleEl = document.getElementById("step-title");
  var hintEl = document.getElementById("required-hint");
  var backButton = document.getElementById("back-button");
  var continueButton = document.getElementById("continue-button");
  var submitButton = document.getElementById("submit-button");
  var stepLabels = ["Your profile", "Media & analytics", "Your partnership"];
  var step = 0;

  if (!form || !success || !resetButton) {
    return;
  }

  function setError(message) {
    if (!message) {
      errorEl.textContent = "";
      errorEl.setAttribute("hidden", "");
      return;
    }
    errorEl.textContent = message;
    errorEl.removeAttribute("hidden");
  }

  function setTitle(label) {
    titleEl.textContent = "";
    titleEl.appendChild(document.createTextNode(label));
    var mark = document.createElement("i");
    mark.textContent = ".";
    titleEl.appendChild(mark);
  }

  function showStep(nextStep) {
    step = nextStep;
    var panes = form.querySelectorAll("[data-step]");
    var index;
    for (index = 0; index < panes.length; index += 1) {
      var pane = panes[index];
      if (Number(pane.getAttribute("data-step")) === step) {
        pane.removeAttribute("hidden");
      } else {
        pane.setAttribute("hidden", "");
      }
    }

    var tabs = form.querySelectorAll(".steps span");
    for (index = 0; index < tabs.length; index += 1) {
      if (index === step) {
        tabs[index].className = "active";
      } else if (index < step) {
        tabs[index].className = "complete";
      } else {
        tabs[index].className = "";
      }
    }

    countEl.textContent = "STEP " + (step + 1) + " OF 3";
    setTitle(stepLabels[step]);

    if (step === 0) {
      hintEl.removeAttribute("hidden");
      backButton.setAttribute("hidden", "");
    } else {
      hintEl.setAttribute("hidden", "");
      backButton.removeAttribute("hidden");
    }

    if (step < 2) {
      continueButton.removeAttribute("hidden");
      submitButton.setAttribute("hidden", "");
    } else {
      continueButton.setAttribute("hidden", "");
      submitButton.removeAttribute("hidden");
    }
  }

  function validateCurrentStep() {
    var pane = form.querySelector('[data-step="' + step + '"]');
    var fields = pane.querySelectorAll("input, select, textarea");
    var index;
    for (index = 0; index < fields.length; index += 1) {
      if (!fields[index].reportValidity()) {
        return false;
      }
    }
    return true;
  }

  function advance() {
    if (!validateCurrentStep()) {
      return;
    }
    setError("");
    showStep(step + 1);
  }

  continueButton.addEventListener("click", advance);

  backButton.addEventListener("click", function () {
    setError("");
    showStep(step - 1);
  });

  form.addEventListener("submit", function (event) {
    event.preventDefault();

    if (step < 2) {
      advance();
      return;
    }

    var fields = form.querySelectorAll("input, select, textarea");
    var index;
    for (index = 0; index < fields.length; index += 1) {
      var field = fields[index];
      if (!field.checkValidity()) {
        var pane = field.closest("[data-step]");
        if (pane) {
          showStep(Number(pane.getAttribute("data-step")));
        }
        setError("Please complete all required fields before submitting.");
        return;
      }
    }

    var data = new FormData(form);
    var mediaLink = String(data.get("mediaLink") || "").trim();
    var media = data.get("media");
    if (!mediaLink && !(media instanceof File && media.size > 0)) {
      showStep(1);
      setError("Please attach your media kit or provide a shareable link.");
      return;
    }

    var analyticsLink = String(data.get("analyticsLink") || "").trim();
    var analyticsFiles = data.getAll("analytics");
    var hasAnalyticsFile = false;
    for (index = 0; index < analyticsFiles.length; index += 1) {
      var file = analyticsFiles[index];
      if (file instanceof File && file.size > 0) {
        hasAnalyticsFile = true;
      }
    }
    if (!analyticsLink && !hasAnalyticsFile) {
      showStep(1);
      setError("Please attach post analytics or provide a shareable report link.");
      return;
    }

    setError("");

    // TODO: Submit this application to the GoHighLevel form endpoint.
    // Do not POST this FormData anywhere until that endpoint is added.
    // Send every field from #application, including the media kit and analytics files.
    // After a successful response, keep this on-page confirmation and show the
    // reference id when GoHighLevel returns one.

    form.setAttribute("hidden", "");
    success.removeAttribute("hidden");
    success.focus();
  });

  resetButton.addEventListener("click", function () {
    form.reset();
    setError("");
    showStep(0);
    success.setAttribute("hidden", "");
    form.removeAttribute("hidden");
    titleEl.focus();
  });

  showStep(0);
})();
