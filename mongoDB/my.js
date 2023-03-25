for(let i=0;i<10;i++)
{
    db.Stores.insertOne({'just id':i})
}

//  use this with load('filename.js') in mongosh shell