try {
  function generateHeroName() {
    const adjective = document.getElementById("adjective").value;
    const animal = document.getElementById("animal").value;
    const title = document.getElementById("title");
    title.innerHTML = "Your hero name is " + adjective + animal;
  }
} catch (er) {
  console.error(er.toString());
}
