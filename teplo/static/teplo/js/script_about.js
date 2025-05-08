// Slider
const handleImgChange1 = (offset) => {
    const activeSlide = document.querySelector("[data-active1]");
    const slides = [...document.querySelectorAll(".slide-1")];
    const currentIndex = slides.indexOf(activeSlide);

    let newIndex = currentIndex + offset;

    if (newIndex < 0) { 
      newIndex = slides.length - 1;
    }
    
    if (newIndex >= slides.length) { 
      newIndex = 0;
    }

    slides[newIndex].dataset.active1 = true;
    delete activeSlide.dataset.active1;
}

const onPrev1 = () => {
    handleImgChange1(-1);
}

const onNext1 = () => {
    handleImgChange1(1);
}

const handleImgChange2 = (offset) => {
    const activeSlide = document.querySelector("[data-active2]");
    const slides = [...document.querySelectorAll(".slide-2")];
    const currentIndex = slides.indexOf(activeSlide);

    let newIndex = currentIndex + offset;

    if (newIndex < 0) { 
      newIndex = slides.length - 1;
    }
    
    if (newIndex >= slides.length) { 
      newIndex = 0;
    }

    slides[newIndex].dataset.active2 = true;
    delete activeSlide.dataset.active2;
}

const onPrev2 = () => {
    handleImgChange2(-1);
}

const onNext2 = () => {
    handleImgChange2(1);
}

const handleImgChange3 = (offset) => {
    const activeSlide = document.querySelector("[data-active3]");
    const slides = [...document.querySelectorAll(".slide-3")];
    const currentIndex = slides.indexOf(activeSlide);

    let newIndex = currentIndex + offset;

    if (newIndex < 0) { 
      newIndex = slides.length - 1;
    }
    
    if (newIndex >= slides.length) { 
      newIndex = 0;
    }

    slides[newIndex].dataset.active3 = true;
    delete activeSlide.dataset.active3;
}

const onPrev3 = () => {
    handleImgChange3(-1);
}

const onNext3 = () => {
    handleImgChange3(1);
}
