index_html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title></title>
    <style>
        .post {
            text-align: center;
            width: 40%;
            min-width: 200px;
            margin: 0 auto;
            margin-bottom: 5px;
            padding: 5px;
            border: 5px solid green;
            border-radius: 10px;
            font-size: 1.5em;
            font-weight: bold;
            color: green;
            background-color: yellow;
        }
    </style>
</head>
<body>
    {{ all_posts_html }}
</body>
</html>
'''
