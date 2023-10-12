from typing import List
import rclpy
from rclpy.context import Context
from rclpy.node import Node
from rclpy.parameter import Parameter



class DefaultNode(Node):
    # node_name (str): 노드의 이름입니다. 모든 노드는 고유한 이름을 가져야 합니다.

    # context (Context): ROS 2의 실행 컨텍스트입니다. 특정한 컨텍스트를 제공하지 않으면 기본 컨텍스트가 사용됩니다.

    # cli_args (List[str]): 명령행 인수 목록입니다. 일반적으로 ROS 노드를 시작할 때 전달된 인수입니다.

    # namespace (str): 노드의 네임스페이스입니다. 네임스페이스를 통해 유사한 노드들을 그룹화할 수 있습니다.

    # use_global_arguments (bool): 전역 인수를 사용할지 여부를 결정합니다.

    # enable_rosout (bool): rosout 로깅을 활성화할지 여부를 결정합니다.

    # start_parameter_services (bool): 파라미터 서비스를 시작할지 여부를 결정합니다. 파라미터 서비스는 노드의 파라미터를 동적으로 변경하고 가져오는데 사용됩니다.

    # parameter_overrides (List[Parameter]): 노드 파라미터에 대한 오버라이드 목록입니다.

    # allow_undeclared_parameters (bool): 선언되지 않은 파라미터의 사용을 허용할지 결정합니다.

    # automatically_declare_parameters_from_overrides (bool): 오버라이드에서 자동으로 파라미터를 선언할지 여부를 결정합니다.
    def __init__(
            self, 
            node_name: str, 
            *, 
            context: Context = None, 
            cli_args: List[str] = None, 
            namespace: str = None, 
            use_global_arguments: bool = True, 
            enable_rosout: bool = True, 
            start_parameter_services: bool = True, 
            parameter_overrides: List[Parameter] = None, allow_undeclared_parameters: bool = False, automatically_declare_parameters_from_overrides: bool = False
            ) -> None:
        super().__init__(
            node_name, 
            context=context, 
            cli_args=cli_args, 
            namespace=namespace, 
            use_global_arguments=use_global_arguments, enable_rosout=enable_rosout, start_parameter_services=start_parameter_services, parameter_overrides=parameter_overrides, allow_undeclared_parameters=allow_undeclared_parameters, automatically_declare_parameters_from_overrides=automatically_declare_parameters_from_overrides
            )

