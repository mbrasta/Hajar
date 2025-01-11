<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Hajaaaayyyy</title>
  <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
  <style>
    /* Global reset and font */
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    body {
      font-family: 'Roboto', sans-serif;
      background: #f1f2f6;
      color: #333;
      text-align: center;
      padding: 50px 0;
    }

    h1 {
      font-size: 42px;
      color: #2c3e50;
      margin-bottom: 40px;
      letter-spacing: 2px;
      font-weight: 700;
    }

    .grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 20px;
      max-width: 900px;
      margin: 0 auto;
      padding-bottom: 50px;
    }

    button {
      padding: 20px 40px;
      font-size: 20px;
      cursor: pointer;
      background-color: #3498db;
      color: white;
      border: none;
      border-radius: 12px;
      transition: all 0.3s ease;
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    }

    button:hover {
      background-color: #2980b9;
      transform: translateY(-5px);
      box-shadow: 0 6px 18px rgba(0, 0, 0, 0.2);
    }

    button:active {
      transform: translateY(0);
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    }

    .picture-container {
      margin-top: 40px;
      display: flex;
      justify-content: center;
    }

    img {
      width: 350px;
      height: auto;
      display: none;
      border-radius: 12px;
      box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
      transition: transform 0.3s ease, box-shadow 0.3s ease;
    }

    img:hover {
      transform: scale(1.1);
      box-shadow: 0 12px 24px rgba(0, 0, 0, 0.2);
    }

    /* Responsive Design */
    @media (max-width: 800px) {
      .grid {
        grid-template-columns: 1fr 1fr;
      }

      h1 {
        font-size: 32px;
      }

      button {
        padding: 15px 30px;
        font-size: 18px;
      }

      img {
        width: 300px;
      }
    }

    @media (max-width: 500px) {
      .grid {
        grid-template-columns: 1fr;
      }

      h1 {
        font-size: 28px;
      }

      button {
        padding: 12px 25px;
        font-size: 16px;
      }

      img {
        width: 250px;
      }
    }
  </style>
</head>
<body>

  <h1>Hajay core:</h1>

  <div class="grid">
    <button onclick="showPicture('animal')">Animal</button>
    <button onclick="showPicture('place')">Place</button>
    <button onclick="showPicture('plant')">Plant</button>
    <button onclick="showPicture('character')">Character</button>
    <button onclick="showPicture('season')">Season</button>
    <button onclick="showPicture('hobby')">Hobby</button>
    <button onclick="showPicture('food')">Food</button>
    <button onclick="showPicture('colour')">Colour</button>
    <button onclick="showPicture('drink')">Drink</button>
  </div>

  <div class="picture-container">
    <img id="picture" alt="Category Image">
  </div>

  <script>
    function showPicture(category) {
      const picture = document.getElementById('picture');
      const images = {
        animal: 'https://i.pinimg.com/736x/da/48/c5/da48c53fdf217625a1fdd95b4c233a06.jpg',
        place: 'https://i.pinimg.com/736x/7c/e0/b3/7ce0b34a80e1113d3722acaaa6e92bd6.jpg',
        plant: 'https://i.pinimg.com/736x/4f/34/2a/4f342aef76faf6970461902fe6b1dff8.jpg',
        character: 'https://i.pinimg.com/736x/1a/14/a9/1a14a94fb45f54a5554013f7117daf8d.jpg',
        season: 'https://i.pinimg.com/736x/02/24/8e/02248e23dceb1baa02bf7ef0ccdab883.jpg',
        hobby: 'https://i.pinimg.com/736x/27/37/e5/2737e5744efda565dd2ff077a202fac4.jpg',
        food: 'https://i.pinimg.com/736x/71/53/16/7153163ceed65ab4c21e5ea9569eb492.jpg',
        colour: 'https://i.pinimg.com/736x/80/1c/4e/801c4eada010d767046be793942421ac.jpg',
        drink: 'https://i.pinimg.com/736x/98/e5/e8/98e5e863c09f5c7d6afd33ab1ee26105.jpg'
      };
      picture.src = images[category];
      picture.style.display = 'block'; // Makes the image visible
    }
  </script>

</body>
</html>
