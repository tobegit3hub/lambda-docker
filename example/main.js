var main = function(){
    console.log("Run nodejs code");
}

if (require.main === module) {
    main();
}

