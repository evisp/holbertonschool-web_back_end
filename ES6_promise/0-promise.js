function getResponseFromAPI() {
    return new Promise((resolve) => {
      setTimeout(() => {
        resolve();
      }, 10);
    });
  }
  
export default getResponseFromAPI;