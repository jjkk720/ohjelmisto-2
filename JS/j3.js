   function grow(luku) {
            for (let i = 0; i<array.length; i++) {
              array[i]++;
            }
            return;
        }

        const numbers = [5,6,7];
        grow(numbers);
        console.log(numbers[0] + ' ' + numbers[1] + ' ' + numbers[2]);
