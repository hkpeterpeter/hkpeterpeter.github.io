## Personal Homepage

### Overview
- Built using [Hugo](http://gohugo.io/) static site generator
- Used [Bootstrap 4](https://getbootstrap.com/) for responsive layout
- Used [Font Awesome 5](https://fontawesome.com/) icons
- Adopted and modified the [timeline](https://www.w3schools.com/howto/howto_css_timeline.asp) example from w3school


### Environment Setup
- [Install Hugo](https://gohugo.io/getting-started/installing/) globally
- [Install yarn](https://yarnpkg.com/lang/en/docs/install/) globally
- Invoke `yarn` once to install the dependency libraries

### Notes on GitHub page 

The following steps can be done by [GitHub Desktop](https://desktop.github.com/)

```sh
git checkout dev             # Switch to the dev branch
git branch                   # Verify that you are in dev
git pull                     # receive the latest update
```

- `master` branch is used for the deployed website. It is required by **GitHub** for an organization page
- `dev` branch is used for hosting the source codes. 


### How to test the website?

```sh
yarn run debug    # Debug, all draft content will be included
yarn run build    # Build the web site content in the public folder (only non-draft content will be included) 
```

### How to deploy?

Commit changes to the `dev` branch
The following steps can be done by [GitHub Desktop](https://desktop.github.com/)

```sh
git checkout dev     # Switch to the dev branch 
git add .            # Added all changes 
git commit -m [msg]  # Commit all changes to the dev branch 
```

After that, run the following to deploy the `dev` branch to GitHub `master` branch

```sh
yarn run deploy      # Deploy the dev branch to the github page. 
```



