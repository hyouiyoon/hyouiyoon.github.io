// get the ninja-keys element
const ninja = document.querySelector('ninja-keys');

// add the home and posts menu items
ninja.data = [{
    id: "nav-about",
    title: "About",
    section: "Navigation",
    handler: () => {
      window.location.href = "/";
    },
  },{id: "nav-publications",
          title: "Publications",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/publications/";
          },
        },{id: "nav-activities",
          title: "Activities",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/activities/";
          },
        },{id: "nav-news",
          title: "News",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/news/";
          },
        },{id: "nav-cv",
          title: "CV",
          description: "Curriculum Vitae",
          section: "Navigation",
          handler: () => {
            window.location.href = "/cv/";
          },
        },{id: "activities-bachelor-s-graduation",
          title: 'Bachelor’s Graduation',
          description: "2025.02.24Ewha W. Univ., Seoul, Korea",
          section: "Activities",handler: () => {
              window.location.href = "/projects/2025/2025_1/";
            },},{id: "activities-ebrl-homecoming",
          title: 'EBRL Homecoming',
          description: "2025.11.14Ewha W. Univ., Seoul, Korea",
          section: "Activities",handler: () => {
              window.location.href = "/projects/2025/2025_2/";
            },},{id: "activities-scholarship-award",
          title: 'Scholarship Award',
          description: "2025.11.16AI SeoulTech Graduate Scholarship",
          section: "Activities",handler: () => {
              window.location.href = "/projects/2025/2025_3/";
            },},{id: "activities-conference-presentation",
          title: 'Conference Presentation',
          description: "2025.11.27-28COSEIK, Daejeon, Korea",
          section: "Activities",handler: () => {
              window.location.href = "/projects/2025/2025_4/";
            },},{id: "activities-conference-presentation",
          title: 'Conference Presentation',
          description: "2025.12.10-13KSME, Gangwon-state, Korea",
          section: "Activities",handler: () => {
              window.location.href = "/projects/2025/2025_5/";
            },},{id: "activities-bk21-workshop",
          title: 'BK21 Workshop',
          description: "2025.12.22Ewha W. Univ., Seoul, Korea",
          section: "Activities",handler: () => {
              window.location.href = "/projects/2025/2025_6/";
            },},{id: "news-university-research-highlight-on-layered-hybrid-lattice-architectures",
          title: 'University Research Highlight on Layered Hybrid Lattice Architectures',
          description: "The study was featured on Ewha Womans University’s official research news platform.",
          section: "News",handler: () => {
              window.location.href = "/news/2026/News_1/";
            },},{
        id: 'social-email',
        title: 'email',
        section: 'Socials',
        handler: () => {
          window.open("mailto:%68%79%6F%75%69%79%6F%6F%6E@%65%77%68%61.%61%63.%6B%72", "_blank");
        },
      },{
        id: 'social-linkedin',
        title: 'LinkedIn',
        section: 'Socials',
        handler: () => {
          window.open("https://www.linkedin.com/in/hyoui-yoon-윤효의-608939367/", "_blank");
        },
      },{
        id: 'social-scholar',
        title: 'Google Scholar',
        section: 'Socials',
        handler: () => {
          window.open("https://scholar.google.com/citations?user=sDgcZ8gAAAAJ", "_blank");
        },
      },{
      id: 'light-theme',
      title: 'Change theme to light',
      description: 'Change the theme of the site to Light',
      section: 'Theme',
      handler: () => {
        setThemeSetting("light");
      },
    },
    {
      id: 'dark-theme',
      title: 'Change theme to dark',
      description: 'Change the theme of the site to Dark',
      section: 'Theme',
      handler: () => {
        setThemeSetting("dark");
      },
    },
    {
      id: 'system-theme',
      title: 'Use system default theme',
      description: 'Change the theme of the site to System Default',
      section: 'Theme',
      handler: () => {
        setThemeSetting("system");
      },
    },];
