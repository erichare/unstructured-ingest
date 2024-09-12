from unstructured_ingest.embed.vertexai import VertexAIEmbeddingConfig, VertexAIEmbeddingEncoder


def test_embed_documents_does_not_break_element_to_dict(mocker):
    # Mocked client with the desired behavior for embed_documents
    mock_client = mocker.MagicMock()
    mock_client.embed_documents.return_value = [1, 2]

    # Mock create_client to return our mock_client
    mocker.patch.object(VertexAIEmbeddingConfig, "get_client", return_value=mock_client)

    encoder = VertexAIEmbeddingEncoder(config=VertexAIEmbeddingConfig(api_key={"api_key": "value"}))
    raw_elements = [{"text": f"This is sentence {i+1}"} for i in range(2)]

    elements = encoder.embed_documents(
        elements=raw_elements,
    )
    assert len(elements) == 2
    assert elements[0]["text"] == "This is sentence 1"
    assert elements[1]["text"] == "This is sentence 2"
