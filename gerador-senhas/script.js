document.addEventListener('DOMContentLoaded', () => {

    const passwordDisplay = document.getElementById('passwordDisplay');
    const lengthInput = document.getElementById('passwordLength');
    const uppercaseCheck = document.getElementById('includeUppercase');
    const numbersCheck = document.getElementById('includeNumbers');
    const symbolsCheck = document.getElementById('includeSymbols');
    const generateButton = document.getElementById('generateButton');
    const copyButton = document.getElementById('copyButton');

    const lowerCaseChars = 'abcdefghijklmnopqrstuvwxyz';
    const upperCaseChars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    const numberChars = '0123456789';
    const symbolChars = '!@#$%^&*()_+=-[]{};:,.<>?/~`';

    function generatePassword(length, includeUpper, includeNums, includeSyms) {
        let availableChars = lowerCaseChars;
        let password = '';
        
        if (includeUpper) {
            availableChars += upperCaseChars;
            password += upperCaseChars.charAt(Math.floor(Math.random() * upperCaseChars.length));
        }
        if (includeNums) {
            availableChars += numberChars;
            password += numberChars.charAt(Math.floor(Math.random() * numberChars.length));
        }
        if (includeSyms) {
            availableChars += symbolChars;
            password += symbolChars.charAt(Math.floor(Math.random() * symbolChars.length));
        }

        if (availableChars.length === lowerCaseChars.length && (includeUpper || includeNums || includeSyms)) {
        }

        const remainingLength = length - password.length;
        for (let i = 0; i < remainingLength; i++) {
            const randomIndex = Math.floor(Math.random() * availableChars.length);
            password += availableChars.charAt(randomIndex);
        }

        password = password.split('').sort(() => Math.random() - 0.5).join('');
        
        return password;
    }

    generateButton.addEventListener('click', () => {
        const length = parseInt(lengthInput.value);
        const includeUpper = uppercaseCheck.checked;
        const includeNums = numbersCheck.checked;
        const includeSyms = symbolsCheck.checked;
        
        if (!includeUpper && !includeNums && !includeSyms) {
            alert("Por favor, selecione pelo menos um tipo de caractere (além de minúsculas) para gerar uma senha mais segura.");
            return;
        }

        const newPassword = generatePassword(length, includeUpper, includeNums, includeSyms);
        passwordDisplay.value = newPassword;
    });
    
    copyButton.addEventListener('click', () => {
        passwordDisplay.select(); 
        passwordDisplay.setSelectionRange(0, 99999); 
        navigator.clipboard.writeText(passwordDisplay.value); 
        
        copyButton.textContent = 'Copiado!'; 
        setTimeout(() => {
            copyButton.textContent = 'Copiar';
        }, 1500);
    });
    
    generateButton.click();
});
